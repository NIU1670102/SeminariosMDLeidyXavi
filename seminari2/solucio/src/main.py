##########################################################################
#########   Classe main del seminari 2 de grafs i complexitat   ##########
#########              Copyright 2022 Bernat Gastón             ##########
#########               Author: Bernat Gastón                   ##########
#########            Contact: bernat.gaston@uab.cat             ##########
#########    Alumnes:                                           ##########
##########################################################################

from graph import Node, Graph
from havelhakimi import havel_hakimi

'''
Funció del exercici 1 per modelar el nou whatsapp amb les relacions donades.
@retorn: El graf representant les relacions donades
'''
def nou_whatsapp():
    pass

'''
Funció del exercici 2 per modelar el instagram amb les relacions donades.
@retorn: El graf representant les relacions donades.
'''
def instagram():
    pass


if __name__ == '__main__':
    #Creem un graf buit
    graph = Graph()
    #Creeem nodes
    node1 = Node('node1', 0, 0)
    node2 = Node('node2', 1, 1)
    #Afegir nodes al graf
    graph.add_node(node1)
    graph.add_node(node2)
    #Afegir arestes
    graph.add_edge(node1, node2)
    #Dibuixem el graf
    graph.draw()
