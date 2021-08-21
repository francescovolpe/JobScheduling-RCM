# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 11:13:36 2021

@author: Francesco
"""

visitati = [] 
coda = []    
attivitaFine = []

def bfsMod(grafo, nodo, tempo_attivita):
    visitati.append(nodo)
    coda.append(nodo)

    while coda:
        s = coda.pop(0)
        attivitaFine.append(s)

        for vicino in grafo[s[0]]:
            vicino = (vicino, (tempo_attivita[vicino] + int(s[1]))  ) 
      
            if vicino not in visitati:
                visitati.append(vicino)
                coda.append(vicino)
    
    return attivitaFine
        

def filtroTempoAttivita(attivitaFine, dizionario_attivita):
    listaSupporto = []
    for x in dizionario_attivita:
        max = 0
        for y in attivitaFine:
            if (y[0] == x) and (y[1] > max):
                max = y[1]
        listaSupporto.append( (x, max) )

    return listaSupporto

    

