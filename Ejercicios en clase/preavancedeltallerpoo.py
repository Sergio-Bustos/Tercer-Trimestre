# # Aqui por lo pronto se subiran los avances que haremos en el taller de POO;



# # Parte 1: Teoria de POO; Ya hecha


# # Parte 2 — Diagramas UML

# # 7. Elige un mini-proyecto (ejemplo: biblioteca, gestión de cursos o tienda online) y responde:

# # ¿Qué clases identificas en el problema? // - Se hace

# # ¿Qué atributos y métodos tendría cada clase? // - Se hace

# # ¿Qué relaciones existen entre ellas? // - Se hace 

# # 8. Realiza un diagrama de clases para el problema elegido. // - Aun no ya que no lo hemos visto detalladamente

# # 9. Crea un diagrama de objetos con instancias concretas de tus clases. // - Aun no ya que no lo hemos visto detalladamente

# # 10. Dibuja un diagrama de secuencia que muestre cómo interactúan los objetos en un caso de uso (ej.: inscribir estudiante, prestar libro, hacer compra). // - Aun no ya que no lo hemos visto detalladamente

# # 11. Dibuja un diagrama de actividad con el flujo de pasos del caso de uso elegido. // - Aun no ya que no lo hemos visto detalladamente

# # Por ahora se hacen mini proyectos de POO,como;


# # Simulador de inventario;



# class Inventario:
#     def __init__(self, producto, precio, fecha_de_compra, fecha_de_vencimiento, fecha_de_produccion, comprador):
#         self.producto = producto
#         self.precio = precio
#         self.fecha_de_compra = fecha_de_compra
#         self.fecha_de_vencimiento = fecha_de_vencimiento
#         self.fecha_de_produccion = fecha_de_produccion
#         self.comprador = comprador

#     def mostrar_info(self):
#         print("Nombre del producto: ", self.producto)
#         print("Precio: ", self.precio)
#         print("Fecha de compra: ", self.fecha_de_compra)
#         print("Fecha de vencimiento: ", self.fecha_de_vencimiento)
#         print("Fecha de producción: ", self.fecha_de_produccion)
#         print("Nombre del comprador: ", self.comprador)


# comprador1 = Inventario(input("Ingresa el producto: "), input("Ingresa el precio: "), input("Ingresa la fecha de compra: "), input("Ingresa la fecha de vencimiento: "), input("Ingresa la fecha de producción: "), input("Ingresa el comprador: "))
# comprador2 = Inventario(input("Ingresa el producto: "), input("Ingresa el precio: "), input("Ingresa la fecha de compra: "), input("Ingresa la fecha de vencimiento: "), input("Ingresa la fecha de producción: "), input("Ingresa el comprador: "))
# comprador3 = Inventario(input("Ingresa el producto: "), input("Ingresa el precio: "), input("Ingresa la fecha de compra: "), input("Ingresa la fecha de vencimiento: "), input("Ingresa la fecha de producción: "), input("Ingresa el comprador: "))
# comprador4 = Inventario(input("Ingresa el producto: "), input("Ingresa el precio: "), input("Ingresa la fecha de compra: "), input("Ingresa la fecha de vencimiento: "), input("Ingresa la fecha de producción: "), input("Ingresa el comprador: "))
# comprador5 = Inventario(input("Ingresa el producto: "), input("Ingresa el precio: "), input("Ingresa la fecha de compra: "), input("Ingresa la fecha de vencimiento: "), input("Ingresa la fecha de producción: "), input("Ingresa el comprador: "))
# comprador6 = Inventario(input("Ingresa el producto: "), input("Ingresa el precio: "), input("Ingresa la fecha de compra: "), input("Ingresa la fecha de vencimiento: "), input("Ingresa la fecha de producción: "), input("Ingresa el comprador: "))
# comprador7 = Inventario(input("Ingresa el producto: "), input("Ingresa el precio: "), input("Ingresa la fecha de compra: "), input("Ingresa la fecha de vencimiento: "), input("Ingresa la fecha de producción: "), input("Ingresa el comprador: "))
# comprador8 = Inventario(input("Ingresa el producto: "), input("Ingresa el precio: "), input("Ingresa la fecha de compra: "), input("Ingresa la fecha de vencimiento: "), input("Ingresa la fecha de producción: "), input("Ingresa el comprador: "))
# comprador9 = Inventario(input("Ingresa el producto: "), input("Ingresa el precio: "), input("Ingresa la fecha de compra: "), input("Ingresa la fecha de vencimiento: "), input("Ingresa la fecha de producción: "), input("Ingresa el comprador: "))
# comprador10 = Inventario(input("Ingresa el producto: "), input("Ingresa el precio: "), input("Ingresa la fecha de compra: "), input("Ingresa la fecha de vencimiento: "), input("Ingresa la fecha de producción: "), input("Ingresa el comprador: "))

# comprador1.mostrar_info()
# comprador2.mostrar_info()
# comprador3.mostrar_info()
# comprador4.mostrar_info()
# comprador5.mostrar_info()
# comprador6.mostrar_info()
# comprador7.mostrar_info()
# comprador8.mostrar_info()
# comprador9.mostrar_info()
# comprador10.mostrar_info()



# # ¿Qué clases identificas en el problema? 
# print("La clase inventario que permite imprimir mediante un metodo mostrar la informacion de los productos ingresados y comprados por los 10 compradores")

# # ¿Qué atributos y métodos tendría cada clase? 
# print("""La unica y principal clase tendria;
#       ------------- ATRIBUTOS: ----------------
#        - producto; Que es el nombre del producto
#        - precio; Su precio
#        - fecha_de_compra; La fecha en el que el comprador la compro
#        - fecha_de_vencimiento; La fecha en que el producto o se vence o empieza a por asi decirlo degradarse
#        - fecha_de_produccion; La fecha en que cierta empresa fabricante fabrico el producto especifico que se va comprar
#        - comprador; Nombre del comprador
#       ------------- METOODOS: -----------------
#        - mostrar_info(): permite mostrar todos los atributos de manera clara y concisa del inventario para un producto""")

# # ¿Qué relaciones existen entre ellas? 
# print("No hay relaciones entre clases porque solo hay una clase (Inventario) en todo el programa. Para que haya relaciones, debe haber al menos dos o más clases que interactúen entre sí.")









# # Calculadora basica

# class Calculadora:
#     def __init__(self,numero_uno,numero_dos):
#         self.numero_uno = numero_uno
#         self.numero_dos = numero_dos
#     def sumar(self):
#         print(f"{self.numero_uno} + {self.numero_dos} = {self.numero_uno+self.numero_dos}")
#     def restar(self):
#         print(f"{self.numero_uno} - {self.numero_dos} = {self.numero_uno-self.numero_dos}")
#     def multiplicacion(self):
#         print(f"{self.numero_uno} * {self.numero_dos} = {self.numero_uno*self.numero_dos}")
#     def division(self):
#         print(f"{self.numero_uno} / {self.numero_dos} = {self.numero_uno/self.numero_dos}")


# persona1 = Calculadora(int(input("Ingresa el primer numero: ")),int(input("Ingresa el segundo numero: ")))
# persona2 = Calculadora(int(input("Ingresa el primer numero: ")),int(input("Ingresa el segundo numero: ")))
# opcion = input("""Que opcion quieres hacer?
#                1. SUMA
#                2. RESTA
#                3. MULTIPLICACION
#                4. DIVISION
#                : """)
# if opcion == "1":
#     persona1.sumar()
# elif opcion == "2":
#     persona1.restar()
# elif opcion == "3":
#     persona1.multiplicacion()
# elif opcion == "4":
#     persona1.division()
# else:
#     print("No se puede hacer ninguna operacion con ese numero...")


# opcion2 = input("""Que opcion quieres hacer?
#                1. SUMA
#                2. RESTA
#                3. MULTIPLICACION
#                4. DIVISION
#                : """)

# if opcion2 == "1":
#     persona2.sumar()
# elif opcion2 == "2":
#     persona2.restar()
# elif opcion2 == "3":
#     persona2.multiplicacion()
# elif opcion2 == "4":
#     persona2.division()
# else:
#     print("No se puede hacer ninguna operacion con ese numero...")


# # ¿Qué clases identificas en el problema? 
# print("La clase calculadora que es la base para que el usuario pueda realizar accciones como sumar restar etc")

# # ¿Qué atributos y métodos tendría cada clase? 
# print("""La unica y principal clase tendria;
#       ------------- ATRIBUTOS: ----------------
#        - numero_uno; Numero uno que el usuario ingresa
#        - numero_dos; Numero dos que el usuario ingresa
#       ------------- METOODOS: -----------------
#        - sumar(); Permite sumar los dos numeros
#       - restar(); Permite restar los dos numeros
#       - multiplicacion(); Permite multiplicar los numeros
#       - dvision(); Permite dividir los numeros""")

# # ¿Qué relaciones existen entre ellas? 
# print("Ninguna como la anterior,ya que no hay mas de una clase por lo tanto no se relacionan...")










# # # Gestor de productos

# # class Productos:
# #     def __init__(self,nombre,precio,marca,fechaenquesehizo,fechaenquesevence):
# #         self.nombre = nombre
# #         self.precio = precio
# #         self.marca = marca
# #         self.fechaenquesehizo = fechaenquesehizo
# #         self.fechaenquesevence = fechaenquesevence
# #     def comprar(self):
# #         print(f"""Que buena eleccion de producto para comprar!!;
# #             nombre: {self.nombre},
# #             precio: {self.precio},
# #             marca: {self.marca},
# #             fecha en que se hizo: {self.fechaenquesehizo},
# #             fecha en que se vence: {self.fechaenquesevence}""")
# #     def registrar(self):
# #         print(f"""Que buena eleccion de producto!! para el registro;
# #             nombre: {self.nombre},
# #             precio: {self.precio},
# #             marca: {self.marca},
# #             fecha en que se hizo: {self.fechaenquesehizo},
# #             fecha en que se vence: {self.fechaenquesevence}""")
                
# #     def vender(self):
# #         print(f"""Que buena eleccion de producto!! para vender;
# #             nombre: {self.nombre},
# #             precio: {self.precio},
# #             marca: {self.marca},
# #             fecha en que se hizo: {self.fechaenquesehizo},
# #             fecha en que se vence: {self.fechaenquesevence}""")

# # cliente1 = Productos(input("Que producto vas a ingresar: "),input("Ingresa su precio: "),input("Ingresa su marca: "),input("Ingresa su fecha en que se hizo: "),input("Ingresa la fecha en que se vence: "))
# # cliente2 = Productos(input("Que producto vas a ingresar: "),input("Ingresa su precio: "),input("Ingresa su marca: "),input("Ingresa su fecha en que se hizo: "),input("Ingresa la fecha en que se vence: "))
# # cliente3 = Productos(input("Que producto vas a ingresar: "),input("Ingresa su precio: "),input("Ingresa su marca: "),input("Ingresa su fecha en que se hizo: "),input("Ingresa la fecha en que se vence: "))

# # opcion1 = input("""Ingresa una opcion:
# #                 1. COMPRAR
# #                 2. REGISTRAR PARA LA TIENDA
# #                 3. VENDER
# #                 : """)
# # if opcion1 == "1":
# #     cliente1.comprar()
# # elif opcion1 == "2":
# #     cliente1.registrar()
# # elif opcion1 == "3":
# #     cliente1.vender()
# # else:
# #     print("Esa opcion no existe para la gestion de nuestros productos")


# # opcion22 = input("""Ingresa una opcion:
# #                 1. COMPRAR
# #                 2. REGISTRAR PARA LA TIENDA
# #                 3. VENDER
# #                 : """)

# # if opcion22 == "1":
# #     cliente2.comprar()
# # elif opcion22 == "2":
# #     cliente2.registrar()
# # elif opcion22 == "3":
# #     cliente2.vender()
# # else:
# #     print("Esa opcion no existe para la gestion de nuestros productos")


# # opcion3 = input("""Ingresa una opcion:
# #                 1. COMPRAR
# #                 2. REGISTRAR PARA LA TIENDA
# #                 3. VENDER
# #                 : """)
# # if opcion3 == "1":
# #     cliente3.comprar()
# # elif opcion3 == "2":
# #     cliente3.registrar()
# # elif opcion3 == "3":
# #     cliente3.vender()
# # else:
# #     print("Esa opcion no existe para la gestion de nuestros productos")



# # # ¿Qué clases identificas en el problema? 
# # print("La clase Productos, que representa un producto con su información (nombre, precio, marca, fechas) y permite gestionarlo mediante métodos como comprar, registrar o vender.")

# # # ¿Qué atributos y métodos tendría cada clase? 
# # print("""La unica y principal clase tendria;
# #       ------------- ATRIBUTOS: ----------------
# #       - nombre: nombre del producto
# #       - precio: precio del producto
# #       - marca: marca del producto
# #       - fechaenquesehizo: cuándo fue producido
# #       - fechaenquesevence: cuándo vence
# #       ------------- METODOS: -----------------
# #       - comprar(): imprime los datos del producto cuando se va a comprar
# #       - registrar(): imprime los datos al registrar el producto en la tienda
# #       - vender(): imprime los datos al vender el producto""")

# # # ¿Qué relaciones existen entre ellas? 
# # print("No hay relaciones entre clases, ya que el programa solo define una clase (Productos). Todos los objetos (cliente1, cliente2) son instancias de esa misma clase.")







# # Gestor de productos con herencia y polimorfismo

# class Productos:
#     def __init__(self, nombre, precio, marca, fechaenquesehizo, fechaenquesevence):
#         self.nombre = nombre
#         self.precio = precio
#         self.marca = marca
#         self.fechaenquesehizo = fechaenquesehizo
#         self.fechaenquesevence = fechaenquesevence

#     def comprar(self):
#         print(f"""
# Que buena elección de producto para comprar!!
# Nombre: {self.nombre}
# Precio: {self.precio}
# Marca: {self.marca}
# Fecha en que se hizo: {self.fechaenquesehizo}
# Fecha en que se vence: {self.fechaenquesevence}
#         """)

#     def registrar(self):
#         print(f"""
# Producto registrado correctamente:
# Nombre: {self.nombre}
# Precio: {self.precio}
# Marca: {self.marca}
# Fecha en que se hizo: {self.fechaenquesehizo}
# Fecha en que se vence: {self.fechaenquesevence}
#         """)

#     def vender(self):
#         print(f"""
# Producto vendido:
# Nombre: {self.nombre}
# Precio: {self.precio}
# Marca: {self.marca}
# Fecha en que se hizo: {self.fechaenquesehizo}
# Fecha en que se vence: {self.fechaenquesevence}
#         """)


# # 🧩 Clase hija que hereda de Productos
# class ProductoAlimenticio(Productos):
#     def __init__(self, nombre, precio, marca, fechaenquesehizo, fechaenquesevence, calorias):
#         # Heredamos atributos del padre
#         super().__init__(nombre, precio, marca, fechaenquesehizo, fechaenquesevence) # Super permite reutilizar el código de la clase padre sin volver a escribirlo.
#         self.calorias = calorias  # Atributo nuevo de la clase hija

#     # Polimorfismo: redefinimos el método comprar()
#     def comprar(self):
#         print(f"""
# Has comprado un producto alimenticio:
# Nombre: {self.nombre}
# Precio: {self.precio}
# Marca: {self.marca}
# Calorías: {self.calorias}
# Fecha de fabricación: {self.fechaenquesehizo}
# Fecha de vencimiento: {self.fechaenquesevence}
#         """)


# # --- Ejemplos de instancias ---
# cliente1 = Productos("Perfume", "45000", "Aromax", "10/09/2025", "10/09/2030")
# cliente2 = ProductoAlimenticio("Yogurt", "2500", "Alpina", "20/10/2025", "27/10/2025", "120 kcal")
# cliente3 = Productos("Iphone", "14.500.000","Apple","10/08/2024","10/08/2030")
# cliente4 = ProductoAlimenticio("Leche","15.000","Alqueria","10/09/2005","10/06/2025","120 kcal")

# # --- Ejemplo de polimorfismo --- 
# # Cada cliente actua de diferente forma dependiendo del producto que compro; Si es alimenticio o si es un producto electronico
# cliente1.comprar()
# cliente2.comprar()
# cliente3.comprar()
# cliente4.comprar()








# # Gestor de notas

# class Notas:
#   def __init__(self,nombre_completo,colegio,nota_uno,nota_dos,nota_tres):
#         self.nombre_completo = nombre_completo
#         self.colegio = colegio
#         self.nota_uno = nota_uno
#         self.nota_dos = nota_dos
#         self.nota_tres = nota_tres
#         self.promedio = (self.nota_uno+self.nota_dos+self.nota_tres) / 3

#   def perder(self):
#         print("Has perdido tienes un promedio menor de 3.0")
 
#   def ganar(self):
#         print("Has ganado,tu promedio es mayor a 3")

# est1 = Notas(input("Ingresa tu nombre completo: "),input("Ingresa el nombre de tu colegio: "),float(input("Ingresa la nota uno: ")),float(input("Ingresa la nota dos: ")),float(input("Ingresa la nota tres: ")))
# est2 = Notas(input("Ingresa tu nombre completo: "),input("Ingresa el nombre de tu colegio: "),float(input("Ingresa la nota uno: ")),float(input("Ingresa la nota dos: ")),float(input("Ingresa la nota tres: ")))
# est3 = Notas(input("Ingresa tu nombre completo: "),input("Ingresa el nombre de tu colegio: "),float(input("Ingresa la nota uno: ")),float(input("Ingresa la nota dos: ")),float(input("Ingresa la nota tres: ")))


# if est1.promedio >= 3.0:
#     est1.ganar()
# else:
#     est1.perder()

# if est2.promedio >= 3.0:
#     est2.ganar()
# else:
#     est2.perder()

# if est3.promedio >= 3.0:
#     est3.ganar()
# else:
#     est3.perder()


# # ¿Qué clases identificas en el problema? 
# print("""En este programa se identifica una única clase, llamada Notas.
#        Esta clase representa a un estudiante con sus notas y calcula su promedio para saber si gana o pierde el año o la materia.""")
    
# # ¿Qué atributos y métodos tendría cada clase? 
# print("""La unica y principal clase tendria;
#       ------------- ATRIBUTOS: ----------------
#       - nombre_completo: nombre del estudiante
#       - colegio: nombre del colegio
#       - nota_uno, nota_dos, nota_tres: las tres calificaciones
#       - promedio: el promedio de las tres notas (calculado automáticamente)
#       ------------- METOODOS: -----------------
#       - ganar(): muestra un mensaje si el promedio es mayor o igual a 3.0
#       - perder(): muestra un mensaje si el promedio es menor a 3.0""")

# # ¿Qué relaciones existen entre ellas? 
# print("""En este programa no hay relaciones entre clases, ya que solo existe una clase (Notas).
# Todos los estudiantes (est1, est2, est3) son instancias (objetos) de la misma clase, pero no hay otra clase que se relacione con ella """)







# # Conversor de monedas

# class Conversor:
#     def __init__(self, valor1):
#         self.valor1 = valor1
#         self.valor2 = valor1 / 4000  # tasa fija de cambio

#     def pasar(self):
#         print(f"COP {self.valor1} es un total de USD {self.valor2}")


# persona1 = Conversor(float(input("Ingresa la cantidad de COP: ")))

# print("Pasando de COP a USD, danos un momento ;)\n")
# persona1.pasar()

# print("""Solo se identifica una clase, llamada Conversor.
# Esta clase se encarga de convertir una cantidad en pesos colombianos (COP) a dólares estadounidenses (USD) utilizando una tasa fija de cambio (1 USD = 4000 COP).""")
    
# # ¿Qué atributos y métodos tendría cada clase? 
# print("""La unica y principal clase tendria;
#       ------------- ATRIBUTOS: ----------------
#       - valor1: cantidad en pesos colombianos (COP)
#       - valor2: cantidad convertida a dólares (USD), calculada automáticamente al crear el objeto
#       ------------- METOODOS: -----------------
#       - pasar(): imprime en pantalla el resultado de la conversión de COP a USD""")

# # ¿Qué relaciones existen entre ellas? 
# print("""No existen relaciones entre clases, porque el programa solo utiliza una clase (Conversor).
# Todos los datos y la lógica están contenidos dentro de esa única clase, y no hay ninguna interacción con otras clases como Usuario, Moneda, o Transacción.""")


# # Del curso de POO:
# # Crea una clase llamada “Automovil”.
# # Declara al menos tres atributos y tres métodos dentro.
# # Usa los atributos en por lo menos un método
# # Usa parámetros especiales en alguno de los métodos
# # Crea dos instancias y llama a alguno de sus métodos.

# class Automovil:
#     def __init__(self,marca,precio,año_de_fabricacion):
#         self.marca = marca
#         self.precio = precio
#         self.año_de_fabricacion = año_de_fabricacion
#     def conducir(self):
#         print(f" Carro: {self.marca}, Precio: {self.precio}, Año de fabricacion: {self.año_de_fabricacion} esta conduciendo actualmente")
#     def frenar(self):
#         print(f" Carro: {self.marca}, Precio: {self.precio}, Año de fabricacion: {self.año_de_fabricacion} acabó de frenar")
#     def acelerar(self):
#         print(f" Carro: {self.marca}, Precio: {self.precio}, Año de fabricacion: {self.año_de_fabricacion} acabó de acelerar")

# carro1 = Automovil("BMW","1.200.000","2024")
# carro1.frenar()
# carro2 = Automovil("Chevrolet","1.200.000","2024")
# carro2.conducir()
# carro3 = Automovil("Audi","1.400.000.000","2009")
# carro3.acelerar()


# # Maestro del curso de POO:
# class Maestro:
#     def __init__(self,nombre,edad,escuela):
#         self.nombre = nombre
#         self.edad = edad
#         self.escuela = escuela
#     def comer(self):
#         print(f"""
# El profesor: {self.nombre}
# de edad: {self.edad} 
# en la escuela: {self.escuela} esta comiendo su desayuno
# """)
#     def enseñar(self):
#         print(f"""
# El profesor: {self.nombre}
# de edad: {self.edad} 
# en la escuela: {self.escuela} esta enseñando su materia
# """)
#     def enseñar(self):
#         print(f"""
# El profesor: {self.nombre}
# de edad: {self.edad} 
# en la escuela: {self.escuela} esta enseñando su materia
# """)
    
# maestro1 = Maestro("Luis","15","La Milagrosa")
# maestro1.comer()
# maestro2 = Maestro("Carlos","27","Nuestra señora del palmar")
# maestro2.enseñar()
        

         



# Ejemplo de herencia y explicacion de encapsulamiento en la documentacion

# class Animal:
#     def __init__(self, animal, edad, color):
#         self.animal = animal
#         self.edad = edad
#         self.color = color

# # Clase hija que hereda de Animal
# class Gato(Animal):
#     def __init__(self, animal, edad, color, nombre):
#         # Llama al constructor de la clase padre
#         super().__init__(animal, edad, color)
#         self.nombre = nombre # Atributo propio de la clase hija

#     def maullar(self):
#         print(f"El {self.animal} llamado {self.nombre} está maullando y dice: ¡Miau!")

# #  Clase hija que hereda de Animal
# class Perro(Animal):
#     def __init__(self, animal, edad, color, nombre):
#         super().__init__(animal, edad, color)
#         self.nombre = nombre # Se puede ocutlar informacion de encapsulamiento mediante self.__nombre = nombre
#         # Y para acceder a este se podria hacer asi:
#         # def verMinombre(self):
#         # return self.__nombre;

#     def ladrar(self):
#         print(f"El {self.animal} llamado {self.nombre} está ladrando y dice: ¡Guau guau!")

# #  Crear objetos
# masc1 = Gato("Gato", "15 años", "Rojo", "Stuart")
# masc1.maullar()

# masc2 = Perro("Perro", "10 años", "Negro", "Toby")
# masc2.ladrar()


# # Ejemplo con encapsulamiento

# class Carro:
#     def __init__(self,marca,precio,añodefab):
#         self.__marca = marca
#         self.precio = precio
#         self.añodefab = añodefab

#     def conducir(self):
#         print(f""" El carro:
#               de marca {self.__marca},
#               de precio: {self.precio},
#               fabricado en el año: {self.añodefab} esta conduciendo actualmente en la carretera""")
#     def frenar(self):
#         print(f""" El carro:
#               de marca {self.__marca},
#               de precio: {self.precio},
#               fabricado en el año: {self.añodefab} esta frenando actualmente en la carretera""")
#     def verLamarca(self):
#         return self.__marca

# carro1 = Carro("BMW","18.000.000","2025")
# carro1.frenar()
# print(f"Marca del primer carro: {carro1.verLamarca()}")

# carro2 = Carro("BMW","18.000.000","2020")
# carro2.conducir()
# print(f"Marca del segundo carro: {carro2.verLamarca()}")




# class Pastel:
#     def __init__(self,precio,ingredienteprincipal,cocinero):
#         self.precio = precio
#         self.ingredienteprincipal = ingredienteprincipal
#         self.cocinero = cocinero





# # Clase abstracta

# from abc import ABC, abstractmethod # Se importan algunas librerias

# class Persona(ABC): # Se crea la clase basada en una libreria
#     def __init__(self, edad, nombre): # Constructor de la clase
#         self.edad = edad # Atributo edad
#         self.nombre = nombre # Atributo nombre
#         print("Se ha creado a", self.nombre, "de", self.edad) # Mensaje de creacion de la persona

#     @abstractmethod # Metodo abstracto

#     def hablar(self, mensaje): # Constructor del metodo hablar
#         pass

# class Deportista(Persona): # Clase hija que hereda de Persona
#     def __init__(self, edad, nombre, deporte): # Constructor de la clase hija
#         super().__init__(edad, nombre) # Llama al constructor de la clase padre
#         self.deporte = deporte # Atributo deporte; Llama los atributos de la clase padre para sobreescribir otro en Deportista
#         print("Se ha creado a", self.nombre, "de", self.edad) # Mensaje de creacion de la persona deportista

#     def practicarDeporte(self): # Metodo practicarDeporte
#         print(self.nombre, ": voy a practicar", self.deporte) # Mensaje de practica de deporte

#     def verMiDeporte(self): # Metodo verMiDeporte
#         return self.deporte # Retorna el deporte del deportista

#     def hablar(self, mensaje): # Implementacion del metodo hablar
#         print(f"{self.nombre} dice: {mensaje}")     # Mensaje de habla del deportista

# luis = Deportista("18", "Luis", "natacion")     # Creacion de un objeto de la clase Deportista
# luis.hablar("Hola soy Sergio el amigo de Luis")    # Llamada al metodo hablar
# luis.practicarDeporte() # Llamada al metodo practicarDeporte
# print("Luis practica", luis.verMiDeporte()) # Llamada al metodo verMiDeporte





# # III.	Usa tu IDE para crear dos subclases de la siguiente clase :

# class Animal: # Clase base Animal
#     def __init__(self): # Constructor de la clase Animal
#         print("Ha nacido un animal!") # Mensaje de creacion del animal
#     def rugir(self): # Metodo rugir
#         print ("Y hace un ruido") # Mensaje de rugido del animal


# class Perro(Animal): # Clase hija Perro que hereda de Animal
#     def __init__(self): # Constructor de la clase Perro
#         super().__init__() # Llama al constructor de la clase padre
#         print("Ha nacido un perro") # Mensaje de creacion del perro
#     def rugir(self): # Metodo rugir sobreescrito
#         print("El perro ladra: ¡Guau guau!")   # Mensaje de ladrido del perro





# # IV.	Crea dos subclases de	“FiguraRegular” que definan el método para calcular su área respectiva según el número de lados, y almacenarla en el atributo “area”. Crea una instancia de cada una.

# class FiguraRegular(ABC): # Clase base FiguraRegular
#     def __init__(self, num_lados): # Constructor de la clase FiguraRegular
#         self.num_lados = num_lados # Atributo num_lados
#         self.area = 0 # Atributo area inicializado en 0

#     @abstractmethod # Metodo abstracto para calcular el area
#     def calcular_area(self):
#         pass
# class Cuadrado(FiguraRegular): # Clase hija Cuadrado que hereda de FiguraRegular
#     def __init__(self, lado): # Constructor de la clase Cuadrado
#         super().__init__(4) # Llama al constructor de la clase padre con 4 lados
#         self.lado = lado # Atributo lado

#     def calcular_area(self): # Metodo para calcular el area del cuadrado
#         self.area = self.lado ** 2 # Calcula el area del cuadrado
#         return self.area # Retorna el area calculada
# class Triangulo(FiguraRegular): # Clase hija Triangulo que hereda de FiguraRegular
#     def __init__(self, base, altura): # Constructor de la clase Triangulo
#         super().__init__(3) # Llama al constructor de la clase padre con 3 lados
#         self.base = base # Atributo base
#         self.altura = altura # Atributo altura

#     def calcular_area(self): # Metodo para calcular el area del triangulo
#         self.area = (self.base * self.altura) / 2 # Calcula el area del triangulo
#         return self.area # Retorna el area calculada    
# # Crear instancias y calcular areas
# cuadrado = Cuadrado(5) # Instancia de Cuadrado con lado 5
# print("Área del cuadrado:", cuadrado.calcular_area()) # Imprime el area del cuadrado        
# triangulo = Triangulo(4, 6) # Instancia de Triangulo con base 4 y altura 6
# print("Área del triángulo:", triangulo.calcular_area()) # Imprime el area del triangulo




# # V.	Crea dos implementaciones de la siguiente clase abstracta:

# from abc import ABCMeta, abstractmethod # Se importan algunas librerias
# class Transporte:       # Clase base Transporte
#  metaclass  = ABCMeta   # Define la metaclase para Transporte
# def  init (self, medio): self.medio = medio         # Constructor de la clase Transporte
# #Usar el atributo "medio" para definir como avanza
# @abstractmethod
# def avanzar(self, frase): pass   # Metodo abstracto avanzar
# def giraIzquierda(self): # Metodo giraIzquierda
#    print("Gira a la izquierda")
# def giraDerecha(self):  # Metodo giraDerecha
#    print("Gira a la derecha")

# #De acuerdo al "medio" especificar que hace para frenar
# @abstractmethod
# def detener(self): pass       # Clase hija Bicicleta que hereda de Transporte
# class Bicicleta(Transporte): # Clase hija Bicicleta que hereda de Transporte
#  def  init (self): # Constructor de la clase Bicicleta
#    super(). init ("terrestre") # Llama al constructor de la clase padre con medio "terrestre"
#  def avanzar(self, frase): # Metodo para avanzar la bicicleta
#    print (f"La bicicleta avanza pedaleando: {frase}")# Mensaje de avance de la bicicleta
#  def detener(self): #    Metodo para detener la bicicleta
#    print ("La bicicleta frena con los frenos de mano") # Mensaje de detencion de la bicicleta
# class Barco(Transporte): # Clase hija Barco que hereda de Transporte
#  def  init (self): # Constructor de la clase Barco
#    super(). init ("acuático") # Llama al constructor de la clase padre con medio "acuático"
#  def avanzar(self, frase): # Metodo para avanzar el barco
#    print (f"El barco avanza navegando: {frase}") # Mensaje de avance del barco
#  def detener(self): # Metodo para detener el barco
#    print ("El barco frena con anclas")      # Mensaje de detencion del barco
# # Crear instancias y probar métodos
# bicicleta = Bicicleta()         
# bicicleta.avanzar("Pedaleando fuerte")
# bicicleta.detener()
# barco = Barco()
# barco.avanzar("Remando con fuerza") 
# barco.detener()


# # CLASE PADRE
# class Animal:
#     def __init__(self,nombre,edad): # Constructor de la clase con sus atributos
#         self.nombre = nombre # Atributo 1
#         self.edad = edad # Atributo 2

# # PRIMERA CLASE QUE HEREDA

# class Felino(Animal): # Clase Felino que hereda de padre (Animal)
#     def __init__(self,nombre,edad,raza): # Constructor de la clase
#         super().__init__(nombre,edad) # super().__init__ ayuda a conservar los mismos atributos que la clas padre
#          # Es como pedir ayuda a la clase padre al crear un nuevo objeto en la clase hija. Garantiza que tanto el código de configuración de la clase padre como el de la hija se ejecuten correctamente, garantizando así un inicio perfecto
#         self.raza = raza # Atributo de la propia clase; polimorfismo

#     def maullar(self): # Metodo maullar propio de la clase Felino
#         print(f"El gato de nombre: {self.nombre},de edad: {self.edad} años de raza {self.raza} esta maullando") # Mensaje
# # Instancias de la clase Felino
# gato1 = Felino("Stuart",15,"Negro")
# gato1.maullar()



# # SEGUNDA CLASE QUE HEREDA

# class Canino(Animal): # Clase hija que hereda
#     def __init__(self,nombre,edad,raza): # Constructor de la clase  con los atributos
#         super().__init__(nombre,edad) # Super init nos ayuda a guardar los atributos 
#         self.raza = raza # Atributo propio de la clase canino
#     def ladrar(self): # Metodo ladrar
#         print(f""" El perro 
#               de nombre: {self.nombre}
#               de edad: {self.edad}
#               de raza: {self.raza}
# """)    # Mensaje

# # INSTANCIAS DE LA CLASE
# canino1 = Canino("Sussy",16,"Beagle")
# canino1.ladrar()