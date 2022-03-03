from flask import Flask, render_template

app = Flask(__name__)

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/contacto")
def contacto():
    return render_template("contactos/index.html")



@app.get("/contacto/<contactoId>/edit")
def editarContacto(contactoId):
    suma=2+2
    return render_template("contactos/editar.html", 
         contactoId=contactoId, 
         suma=suma

    )
#/edad/21 Tu naciste en el año 2000
@app.get("/edad/<int:edadId>/edad")
def calculandoEdad(edadId):
  edad=2022-edadId
  return render_template("contactos/edad.html",edad=edad)
    
app.run(debug=True)
#introduccion a FLask para subir