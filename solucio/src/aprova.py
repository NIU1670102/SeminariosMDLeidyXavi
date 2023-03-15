##########################################################################
#########   Classe aprova del seminari 1 de grafs i complexitat   ########
#########              Copyright 2022 Bernat Gastón               ########
#########               Author: Bernat Gastón                     ########
#########            Contact: bernat.gaston@uab.cat               ########
#########            Alumnes:                                     ########
##########################################################################

from random import randint


'''
Funció que genera dos nombres aleatoris entre 1 i num_opcions i els compara. Retorna True si son iguals, False si no ho son.
Simula una resposta aleatoria
@param: número de opcions
@return: True si els nombres son iguals, False si no
'''
def resposta_pregunta(num_opcions):
    return True

'''
Funció que donat un examen de tipus test, calcula les probabilitats d'aprovar empíricament. 
Assumeix que totes les preguntes valen igual, que l'exàmen és sobre 10 i que les preguntes
resten de forma equivalent
@param: num_preguntes: Número de preguntes totals del exàmen
@param num_preguntes_resposes: Número de preguntes correctament resposes
@param num_preguntes_aleatories: Número de preguntes que respondrem aleatoriament
@param num_opcions: Número d'opcions per pregunta
'''
def fes_examens(num_preguntes, num_preguntes_resposes, 
                        num_preguntes_aleatories, num_opcions):
    #Init variables
    #Calcula nota sense preguntes aleatories
    #Fes 100.000 intents, calcula respostes aleatories i comprova aprovat o suspes
    return 0


'''
OPCIONAL Funció que donat un examen de tipus test, calcula les probabilitats d'aprovar empíricament. 
Assumeix que totes les preguntes valen igual, que l'exàmen és sobre 10 i que les preguntes
resten de forma equivalent.
@param: num_preguntes: Número de preguntes total del exàmen
@param num_preguntes_resposes: Número de preguntes correctament resposes
@param preguntes_aleatories: Llista amb el nombre d’opcions en les quals dubteu per a cada pregunta aleatòria
@param num_opcions: Número d'opcions per pregunta
'''
def fes_examens_descarta_opcions(num_preguntes, num_preguntes_resposes, 
                        preguntes_aleatories, num_opcions):
    return 0