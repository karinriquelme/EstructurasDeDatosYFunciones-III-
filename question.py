import preguntas as p
import random
from shuffle import shuffle_alt

# Opciones dadas para escoger.
###############################################
opciones = {'basicas': [1,2,3],
            'intermedias': [1,2,3],
            'avanzadas': [1,2,3]}
###############################################

def choose_q(dificultad):
    #escoger preguntas por dificultad
    preguntas = p.pool_preguntas[dificultad]
    
    # usar opciones desde ambiente global
    global opciones
    # escoger una pregunta
    n_elegido = random.randint(0, len(list(opciones[dificultad]))-1) 
    # eliminarla del ambiente global para no escogerla de nuevo
    
    preguntas_elegidas = list(preguntas.keys())
    preguntas_dic = list(preguntas.items())
    
    if n_elegido == 0:
        indice_dic = preguntas_elegidas[0]
    elif n_elegido == 1:
        indice_dic = preguntas_elegidas[1] 
    else:
        indice_dic = preguntas_elegidas[2]
        
    del preguntas[indice_dic]  
    
    preguntas_elegida = preguntas_dic[n_elegido]
    
    del opciones[dificultad][n_elegido]
    
    # escoger enunciado y alternativas mezcladas
    
    n_elegido_azar = shuffle_alt(preguntas_elegida[1])
    
    pregunta = f"pregunta: {preguntas_elegida[1]['enunciado'][0]}" 
    alternativas = [value for value in n_elegido_azar] 
    
    
    return pregunta, alternativas

if __name__ == '__main__':
    # si ejecuto el programa, las preguntas cambian de orden, pero nunca debieran repetirse
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')