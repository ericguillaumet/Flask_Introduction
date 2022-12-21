from flask import Flask, render_template #Import Flask library

app = Flask(__name__) #Metodo para usar la función Flask en la app

#Para inicializar el servidor(Flask) tenemos que agregar un valor:
#En Mac: export FLASK_APP=hello.py (hacemos correr el archivo Flask) // sin espacios
#En Windows: set FLASK_APP=hello.py
#Comando para ejecutar el servidor: flask --app hello run
#Comando para actualizar el servidor con cambios de código en tiempo real: flask --app hello --debug run
#Comando especial para lanzar el servidor en un puerto diferente:
#Esto se utiliza en el caso que el puerto 5000 esté ocupado.
#flask --app hello run -p 5001
#Comando para lanzar modo debug en el puerto cambiado:
#flask --app hello --debug run -p 5001

@app.route("/hello") #Definimos la ruta donde vamos a ejecutar la función
def hello_world(): #Retorna un string "Hello World"
    return "Hello world Flask"

#Ejercicio: crear una ruta "adiós" que retorne una despedida, por ejemplo: Hasta pronto Rolando

@app.route("/seeyou")
def seeyou():
    return "See you later Rolando"

#Ejemplo para enviar parámetros en las rutas
@app.route("/name/<n>")
def name(n):
    return f"Your name is {n}"

#Ejercicio realizar una ruta con parámetro que devuelva un número al cuadrado:
@app.route("/number/<n>")
def square(n):
    num = int(n)*int(n)
    return f"The square of {n} is {num}"

@app.route("/number/<int:n1>/<int:n2>")
def addition(n1, n2):
    return f"The addition equals {n1 + n2}"

#Ejercicio realizar una ruta que dinamicamente pueda solicitar realizar
#operaciones de suma, resta, multiplicación y división según los parámetros
#pasados por ruta url

@app.route("/operations/<float:n1>/<float:n2>/<op>") #op = operación 
#Al haberlo establecido como float, al servidor debemos pasarselo como tal.
def calculator(n1, n2, op):
    if op == "addition":
        return render_template("hello.html", result = f"The addition of {n1} and {n2} equals {n1 + n2}")
    elif op == "subtraction":
        return render_template("hello.html", result = f"The subtraction of {n1} and {n2} equals {n1 - n2}")
    elif op == "multiplication":
        return render_template("hello.html", result = f"The multiplication of {n1} and {n2} equals {n1 * n2}")
    elif op == "division":
        return render_template("hello.html", result = f"The division of {n1} and {n2} equals {n1 / n2}")

@app.route("/primerhtml/<nombre>")
def callhtml(nombre):
    return render_template("hello.html",name = nombre)
"""
@app.route("/firsthtml/<nombre>")
def callhtml(nombre):
    return render_template("hello.html", name = nombre)
"""