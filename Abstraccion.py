from abc import ABC, abstractmethod

# Clase abstracta
class Vehiculo(ABC):
    def __init__(self, marca, modelo, año, color):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color

    def __str__(self):
        return f"Vehículo genérico: {self.marca} {self.modelo} ({self.año}) - Color: {self.color}"


# Subclases que heredan solo los atributos
class Auto(Vehiculo):
    pass


class Moto(Vehiculo):
    pass


class Camion(Vehiculo):
    pass


class Helicoptero(Vehiculo):
    pass





# Crear objetos de las clases hijas
auto1 = Auto("Toyota", "Corolla", 2022, "Rojo")
moto1 = Moto("Yamaha", "FZ", 2021, "Negra")
camion1 = Camion("Volvo", "FH", 2020, "Blanco")
helicoptero1 = Helicoptero("Bell Helicopter", "Bell 505", "2025", "Verde")
auto2 = Auto("Acura", "Type S", 2007, "Gris")
moto2 = Moto("Italka", "DM", 2021, "Azul")
camion2 = Camion("Chevrolet", "FRR 1121", 2020, "Blanco")
helicoptero2 = Helicoptero("Bell Helicopter", "Bell 452", "2025", "Negro")


# Visualización
print(auto1)
print(moto1)
print(camion1)
print(helicoptero1)
print(auto2)
print(moto2)
print(camion2)
print(helicoptero2)