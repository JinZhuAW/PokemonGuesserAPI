import sqlite3

def get_name(pokemon_id):
    with sqlite3.connect("pokedex.sqlite") as conn:
        cursor = conn.cursor()
        cursor.execute(f"""SELECT p.identifier FROM pokemon p
	    WHERE p.id = {pokemon_id}""")
        name = cursor.fetchone()
    return name

def get_moves(pokemon_id):
    with sqlite3.connect("pokedex.sqlite") as conn:
        cursor = conn.cursor()
        cursor.execute(f"""SELECT m.identifier FROM moves m 
        JOIN pokemon_moves pm ON m.id = pm.move_id 
        JOIN pokemon p ON p.id = pm.pokemon_id
	    WHERE p.id = {pokemon_id} AND pm.version_group_id = 1
	    LIMIT 5;""")
        moves = cursor.fetchall()
    return moves

def get_species_flavor_text(pokemon_id):
    with sqlite3.connect("pokedex.sqlite") as conn:
        cursor = conn.cursor()
        cursor.execute(f"""SELECT psft.flavor_text FROM pokemon_species_flavor_text psft
	    JOIN pokemon p ON p.species_id = psft.species_id
	    WHERE p.id = {pokemon_id} AND psft.version_id = 1 
        AND psft.language_id = 9;""")
        flavor_text = cursor.fetchone()
    return flavor_text

