
def validate(opciones, eleccion_val):
    # Definir validación de eleccion
    ##########################################################################
    while eleccion_val not in opciones:
        eleccion_val=input("Opcion no valida, ingrese una de las opcoones validas:")
    
    ##########################################################################
    return eleccion_val


if __name__ == '__main__':
    
    eleccion = input('Ingresa una Opción: ').lower()
    # letras = ['a','b','c','d'] # pueden probar con letras también para verificar su funcionamiento.
    numeros = ['0','1']
    # Si se ingresan valores no validos a eleccion debe seguir preguntando
    validate(numeros, eleccion)
    
    
