import json

biblioteca = {
    "978-84-376-0494-7": {
        "título": "Amor de viejo",
        "autor": ["Ireneo Paz"],
        "géneros": ["Romance"]
    },
    "978-84-204-1625-5": {
        "título": "Angelina",
        "autor": ["Rafael Delgado"],
        "géneros": ["Romance"]
    },
        "978-84-670-4952-2": {
        "título": "Carmen",
        "autor": "Pedro Castera",
        "géneros": ["Drama"]
    },
    "978-84-376-0493-0": {
        "título": "Vulcano",
        "autor": "Frias y Soto",
        "géneros": ["Novela corta"]
    },
    "978-84-204-6837-7": {
        "título": "¡Carne de cañon!",
        "autor": "Marcelino Davalos",
        "géneros": ["Romance"]
    }
}

isbn = "978-84-376-0493-0"
info_libro = biblioteca.get(isbn)          
print("\nInformación del libro:",info_libro)