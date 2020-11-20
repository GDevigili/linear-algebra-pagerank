import re, sys, math, csv, types
import random as rd
import networkx as nx
from collections import defaultdict


def parse(filename):
    
    file = csv.reader(open(filename, 'r'), delimiter=',')
    data = [row for row in file]
    
    print("Reading data")
    
    G = nx.Graph()                                          
    nodes = set([row[0] for row in data])                   # (1)-->
    edges = [(row[0], row[2]) for row in data]              # (2)-->

    nbr_of_nodes = len(nodes)
    rank = 1/float(nodes)                                   # (3)-->

    G.add_nodes_from(nodes, rank=rank)
    G.add_edges_from(edges)
    
    return G
    # -->(1) Define a set with the unique state names
    # -->(2) Define a list with containing the 
    # -->(3) Define the rank value for each link
    

def digits(val):
    return int(re.sub("\D", "", val))


def format_key(key): #cleans the key string
    key = key.strip()
    if key.startswith('"') and key.endswith('"'):
        key = key[1:-1]
    return key


def print_results(f, method, results):
    print(method)
