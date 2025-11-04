## -*- coding: utf-8 -*-

class Alumno:
    # Clase que representa a un alumno de la universidad

    def __init__(self, nombre: str, numero_control: str, carrera=None, semestre: int = 1):
        # Atributos del alumno:
        self.nombre = nombre                  # Nombre completo del alumno
        self.numero_control = numero_control  # Número de control del alumno
        self.carrera = carrera                # Carrera de el alumno
        self.calificaciones = {}              # Diccionario que guarda las calificaciones por materia
        self.semestre = semestre              # Nuevo atributo: semestre actual en el que esta el alumno

    def asignar_carrera(self, carrera):
        self.carrera = carrera

    def consulta_calificacion(self, nombre_materia: str):
        if nombre_materia in self.calificaciones:
            return self.calificaciones[nombre_materia]
        else:
            return f'No hay calificación registrada para "{nombre_materia}".'

    def __repr__(self):
        return f'Alumno("{self.nombre}", "{self.numero_control}", semestre={self.semestre})'


class Universidad:
    # Clase que representa una universidad

    def __init__(self, nombre: str):
        # Atributos de la universidad:
        self.nombre = nombre       # Nombre de la universidad
        self.carreras = []         # Lista de carreras que ofrece
        self.alumnos = []          # Lista de alumnos registrados
        self.profesores = []       # Lista de profesores que imparten materias

    # ------------------- Gestión de carreras -------------------
    def agregar_carrera(self, carrera):
        self.carreras.append(carrera)

    def obtener_carrera(self, nombre_carrera: str):
        for c in self.carreras:
            if c.nombre == nombre_carrera:
                return c
        return None

    # ------------------- Otros registros -------------------
    def agregar_alumno(self, alumno):
        self.alumnos.append(alumno)

    def agregar_profesor(self, profesor):
        self.profesores.append(profesor)


class Carrera:
    # Clase que representa una carrera o programa académico

    def __init__(self, nombre: str):
        # Atributos de la carrera:
        self.nombre = nombre       # Nombre de la carrera
        self.materias = []         # Lista de materias que pertenecen a esta carrera

    def agregar_materia(self, materia):
        self.materias.append(materia)

    def obtener_materia(self, nombre_materia: str):
        for m in self.materias:
            if m.nombre == nombre_materia:
                return m
        return None

    def __repr__(self):
        return f'Carrera("{self.nombre}")'


class Materia:
    # Clase que representa una materia

    def __init__(self, nombre: str, carrera: Carrera, calificacion_final: float = None):
        # Atributos de la materia:
        self.nombre = nombre                 # Nombre de la materia
        self.carrera = carrera               # Carrera a la que pertenece
        self.calificacion_final = calificacion_final  # Calificación final de la materia

    def __repr__(self):
        return f'Materia("{self.nombre}", carrera="{self.carrera.nombre}")'


class Profesor:
    # Clase que representa a un profesor

    def __init__(self, nombre: str, materia: Materia):
        # Atributos del profesor:
        self.nombre = nombre         # Nombre del profesor
        self.materia = materia       # Materia que da

    def registra_calificacion(self, alumno: Alumno, calificacion: float):
        alumno.calificaciones[self.materia.nombre] = calificacion
        print(f'Calificación registrada: {alumno.nombre} -> '
              f'{self.materia.nombre}: {calificacion}')

    def __repr__(self):
        return f'Profesor("{self.nombre}", {self.materia})'


# ------------------- Inicio de el programa -------------------
if __name__ == "__main__":

    uni = Universidad("Instituto")

    ing = Carrera("Ingeniería")
    lic = Carrera("Licenciatura en Ciencias Sociales")

    uni.agregar_carrera(ing)
    uni.agregar_carrera(lic)

    calc = Materia("Cálculo I", ing)
    fis = Materia("Física I", ing)
    sociologia = Materia("Introducción a la Sociología", lic)

    ing.agregar_materia(calc)
    ing.agregar_materia(fis)
    lic.agregar_materia(sociologia)

    juan = Alumno("Juan Pérez", "2023001", semestre=2)
    luisa = Alumno("Luisa Gómez", "2023002", semestre=3)

    juan.asignar_carrera(ing)
    luisa.asignar_carrera(ing)

    uni.agregar_alumno(juan)
    uni.agregar_alumno(luisa)

    prof_garcia = Profesor("Dr. García", calc)
    prof_rodriguez = Profesor("Mtra. Rodríguez", fis)

    uni.agregar_profesor(prof_garcia)
    uni.agregar_profesor(prof_rodriguez)

    prof_garcia.registra_calificacion(juan, 8.5)
    prof_garcia.registra_calificacion(luisa, 9.0)
    prof_rodriguez.registra_calificacion(juan, 7.5)

    print(juan.consulta_calificacion("Cálculo I"))   
    print(juan.consulta_calificacion("Física I"))   
    print(luisa.consulta_calificacion("Cálculo I")) 
    print(luisa.consulta_calificacion("Física I"))  

    print("Materias de Ingeniería:", [m.nombre for m in ing.materias])
