import re, sys, math, csv, types
import random as rd
import networkx as nx
from collections import defaultdict

def parse(filename, isDirected):
    # Open the file in read mode
    file = csv.reader(open(filename, 'r'), delimiter=',')
    data = [row for row in file]
    
    print("Reading data")
    
    if isDirected:
        return parse_directed(data)
    else:
        return parse_undirected(data)

