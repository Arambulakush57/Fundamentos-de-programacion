import json

biblioteca = {
    "978-84-376-0494-7": {
        "título": "Cien años de soledad",
        "autor": ["Gabriel García Márquez"],
        "géneros": ["Realismo mágico", "Novela histórica"]
    },
    "978-84-204-1625-5": {
        "título": "Don Quijote de la Mancha",
        "autor": ["Miguel de Cervantes Saavedra"],
        "géneros": ["Novela de caballería", "Satira"]
    }
}

isbn = "978-84-376-0494-7"
info_libro = biblioteca.get(isbn)          
print("\nInformación del libro:", info_libro)

# Agrego dos cuentos más a la biblioteca
biblioteca["978-84-7432-0012-3"] = {
    "título": "La noche boca arriba",
    "autor": ["Julio Cortázar"],
    "géneros": ["Cuento", "Realismo fantástico"]
}

biblioteca["978-84-7432-0012-4"] = {
    "título": "El almohadón de plumas",
    "autor": ["Horacio Quiroga"],
    "géneros": ["Cuento", "Terror", "Ficción corta"]
}

print("\nBiblioteca completa:")
print(json.dumps(biblioteca, ensure_ascii=False, indent=2))