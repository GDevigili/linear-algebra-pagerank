import re, sys, math, types
import random as rd
import networkx as nx
from collections import defaultdict

def parse(filename, isDirected):
    """
    

    Parameters
    ----------
    filename : str
        O caminho do arquivo que contém o dataset do qual irá se calcular o pagerank.
    isDirected : bool
        Indica se o gráfico é orientado ou não.

    Returns
    -------
    None.

    """
    
    reader = csv.reader(open(filename, 'r'), delimiter = ',')
    data = [row for row in reader]
    
    print(data)
    
