#Este es un comentario de una sola linea
'''
Este es un comentario de multiple linea con comilla sencilla
'''
"""
Este es un comentario de multiple linea con comilla doble
"""
#Variables
nombrePersona='Jeyson' #String
edad=27 #int
numeroDecimal=10.2 #float
esMayorEdad= True # False boolean primera letra en mayuscula xd

#debug
print(nombrePersona) # Jeyson

#Array Arreglo Listas con [] se identifica el arreglo

diaSemana=['Lunes','Lartes', 'Miercoles','Jueves']
print(diaSemana[2])#Miercoles

arrayMultiple=[1, 'hola', [5,6]]
print(arrayMultiple[2][1]) #Numero 6 llamar arreglo dentro de otro xd
'''
arrayMultiples=[1, 'hola', [5,6[7,8]]]
print(arrayMultiples[2][2][1])#8
'''
#Objetos  json con diccionario {}
persona={
    'nombre':'Jeyson',
    'apellido':'calvache',
    'edad':27,
    'lenguajes': ['python', 'javascript'],


}
print(persona['nombre'])#jeyson
print(persona['lenguajes'][1])

#Listas de diccionarios
personas=[
    {
    'nombre':'Jeyson',
    'apellido':'calvache',
    'edad':27,
    'lenguajes': ['python', 'javascript'],


},
{
    'nombre':'Carlos',
    'apellido':'Paz',
    'edad':27,
    'lenguajes': ['java', '.net'],


},
{
    'nombre':'Franklin',
    'apellido':'calvache',
    'edad':27,
    'lenguajes': ['python', 'javascript'],


}

]
print(personas[1]['lenguajes'][1])


#condiciones
if esMayorEdad==True:
    print('Es mayor de edad')
else:
    print('No es mayor de edad')
