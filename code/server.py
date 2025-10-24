# Importa el módulo sqlite3 para manejar la base de datos SQLite
import sqlite3
# Importa argparse para manejar argumentos de línea de comandos
import argparse
# Importa FastMCP, el framework del servidor MCP
from mcp.server.fastmcp import FastMCP

# Crea una instancia global de FastMCP con el nombre 'sqlite-demo'
mcp = FastMCP('sqlite-demo')

# Inicializa la base de datos y crea la tabla 'people' si no existe
def init_db():
    conn = sqlite3.connect('../data/demo.db')  # Conexión a la base de datos SQLite
    cursor = conn.cursor()
    # Crea la tabla 'people' si no existe
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS people (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            profession TEXT NOT NULL
        )
    ''')
    conn.commit()
    return conn, cursor

# Herramienta MCP para agregar datos a la tabla 'people' usando parámetros individuales
@mcp.tool()
def add_person(name: str, age: int, profession: str) -> str:
    """
    Inserta un nuevo registro en la tabla 'people' de la base de datos.

    Permite agregar personas a la base de datos proporcionando nombre, edad y profesión.

    Parámetros:
        name (str): Nombre de la persona.
        age (int): Edad de la persona.
        profession (str): Profesión de la persona.

    Retorna:
        str: Mensaje de éxito o error.

    Ejemplo de uso:
        >>> add_person('Cristiano Ronaldo', 41, 'Football Player')
        "Persona 'Cristiano Ronaldo' agregada exitosamente"
    """
    conn, cursor = init_db()
    try:
        cursor.execute(
            "INSERT INTO people (name, age, profession) VALUES (?, ?, ?)",
            (name, age, profession)
        )
        conn.commit()
        return f"Persona '{name}' agregada exitosamente"
    except sqlite3.Error as e:
        return f"Error agregando persona: {e}"
    finally:
        conn.close()

# Herramienta MCP para leer datos de la tabla 'people' 
@mcp.tool()
def get_people(query: str = "SELECT * FROM people") -> list:
    """
    Lee datos de la tabla 'people' de la base de datos usando una consulta SQL SELECT.

    Permite recuperar registros de la tabla 'people' según la consulta SQL proporcionada. 
    Por defecto, devuelve todos los registros.

    Parámetros:
        query (str, opcional): Consulta SQL SELECT. Por defecto es "SELECT * FROM people".

    Retorna:
        list: Lista de diccionarios con los resultados de la consulta.

    Ejemplo de uso:
        >>> get_people()
        [{"id": 1, "name": "John Doe", "age": 30, "profession": "Engineer"}]

        >>> get_people("SELECT name, profession FROM people WHERE age < 30")
        [{"name": "Alice Smith", "profession": "Developer"}]
    """
    conn, cursor = init_db()
    try:
        cursor.execute(query)
        columns = [description[0] for description in cursor.description]
        results = cursor.fetchall()
        
        # Convertir a lista de diccionarios para mejor legibilidad
        return [dict(zip(columns, row)) for row in results]
    except sqlite3.Error as e:
        print(f"Error reading data: {e}")
        return []
    finally:
        conn.close()

# Herramienta MCP para obtener todas las personas (simplificado)
@mcp.tool()
def get_all_people() -> list:
    """
    Obtiene todas las personas de la base de datos.

    Retorna:
        list: Lista de todas las personas con sus detalles.
    """
    return get_people("SELECT * FROM people")

# Herramienta MCP para buscar personas por nombre
@mcp.tool()
def find_person_by_name(name: str) -> list:
    """
    Busca personas por nombre en la base de datos.

    Parámetros:
        name (str): Nombre de la persona a buscar.

    Retorna:
        list: Lista de personas que coinciden con el nombre.
    """
    return get_people(f"SELECT * FROM people WHERE name LIKE '%{name}%'")

# Punto de entrada principal del servidor
if __name__ == "__main__":
    # Imprime mensaje de inicio
    print("🚀Starting server... ")

    # Configura los argumentos de línea de comandos para elegir el tipo de servidor
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--server_type", type=str, default="sse", choices=["sse", "stdio"]
    )

    args = parser.parse_args()
    # Inicia el servidor MCP con el tipo especificado
    mcp.run(args.server_type)