###########################################################################
#########   Classe graph del seminari 2 de grafs i complexitat   ##########
#########              Copyright 2022 Bernat Gastón              ##########
#########               Author: Bernat Gastón                    ##########
#########            Contact: bernat.gaston@uab.cat              ##########
#########     Alumnes:                                           ##########
###########################################################################

import matplotlib.pyplot as plt
from math import trunc

'''
Classe que crea un Node de un graf
'''
class Node:
    '''
    Constructor de classe
    @param: name: nom del node
    @param: x: posició del node en x al gràfic
    @param: y: posició del node en y al gràfic
    '''
    def __init__(self, name, x=0, y=0) -> None:
        self.name = name
        self.edges = list()
        self.set_pose(x, y)
    
    '''
    Redefineix la posició d'un node
    @param: x: posició del node en x al gràfic
    @param: y: posició del node en y al gràfic
    '''    
    def set_pose(self, x, y):
        self.x = x
        self.y = y

    '''
    Calcula el grau d'un node
    A OMPLIR PER L'EXERCICI 1
    @return: Grau del node
    '''
    def degree(self):
        return -1

    '''
    Afegeix una aresta simple. 
    Cal tenir en compte que una aresta simple significa que els dos nodes conectats tenen al altre com a veí 
    A OMPLIR PER L'EXERCICI 1
    @param: node: el node amb el que afegir la aresta
    '''
    def add_simple_edge(self, node):
        pass
    
    '''
    Afegeix una aresta dirigida
    A OMPLIR PER L'EXERCICI 2
    @param: node: el node amb el que afegir la aresta
    '''
    def add_directed_edge(self, node):
        pass

    '''
    Retorna els veins del node
    A OMPLIR PER L'EXERCICI 2
    @retorn una llista amb els nodes veins
    '''
    def neighbours(self):
        return list()

    '''
    Dibuixa el node amb les seves arestes (només per Graf dirigit)
    '''
    def draw_directed(self):
        plt.plot(self.x, self.y, marker='o', markerfacecolor='blue', markersize=12)
        for vei in self.edges:
            plt.arrow(self.x, self.y, vei.x-self.x, vei.y-self.y, width=0.001, 
            head_width=0.05, facecolor='green', length_includes_head=True)

    '''
    Dibuixa el node amb les seves arestes (només per Graf simple)
    '''
    def draw_simple(self):
        for vei in self.edges:
            if self in vei.edges:
                x = [self.x, vei.x]
                y = [self.y, vei.y]
                plt.plot(x, y, color='green', marker='o', markerfacecolor='blue', markersize=12)


'''
Classe que representa un graf
'''
class Graph:
    '''
    Constructor que crea un graf buit
    @param: id_directed: True si el graf és dirigit, False si no
    '''
    def __init__(self, is_directed=False) -> None:
        self.nodes = list()
        self.is_directed = is_directed

    '''
    Afegeix un node al graf
    A OMPLIR PER L'EXERCICI 1
    @param: node: Node a afegir
    '''
    def add_node(self, node):
        pass

    '''
    Treu un node del graf
    A OMPLIR PER L'EXERCICI 1
    '''
    def delete_node(self, node):
        pass

    '''
    Crea una aresta entre dos nodes. Depen de quin tipus de graf tenim
    A OMPLIR AL EXERCICI 1
    A MODIFICAR AL EXERCICI 2
    @param: node1: primer node
    @param node2: segon node
    '''
    def add_edge(self, node1, node2):
        pass

    '''
    Calcula l'ordre del graf
    A OMPLIR PER L'EXERCICI 1
    @return: L'ordre del graf
    '''
    def order(self):
        return -1

    '''
    Calcula la mida d'un graf
    A OMPLIR PER L'EXERCICI 2
    return: La mida del graf
    '''
    def size(self):
        return -1

    '''
    Comprova si dos nodes son veins. Si és dirigit, només calcula si es pot arribar al segon node desde el primer
    A OMPLIR PER L'EXERCICI 2
    @param node1: Primer node
    @param node2: Segon node
    '''
    def is_neighbour(self, node1, node2):
        pass

    '''
    Calcula la sequència gràfica del graf
    A OMPLIR PER L'EXERCICI 2
    @return: La sequència gràfica (ordenada de major a menor)
    '''
    def graphic_sequence(self):
        pass

    '''
    Dibuixa el graf
    '''
    def draw(self):
        for node in self.nodes:
            if self.is_directed:
                node.draw_directed()
            else:
                node.draw_simple()
        plt.show()