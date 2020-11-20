import re, sys, math, csv, types
import random as rd
import networkx as nx
from collections import defaultdict


def parse(filename, isDirected):
    
    file = csv.reader(open(filename, 'r'), delimiter=',')
    data = [row for row in file]
    
    print("Reading data")
    
    if isDirected:
        return parse_directed(data)
    else:
        return parse_undirected(data)


def parse_undirected(data):
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
    

def parse_directed(data):
    DG = nx.DiGraph()

    for i, row in enumerate(data):

        node_a = format_key(row[0])
        node_b = format_key(row[2])
        val_a = digits(row[1])
        val_b = digits(row[3])

        DG.add_edge(node_a, node_b)
        if val_a >= val_b:
            DG.add_path([node_a, node_b])
        else:
            DG.add_path([node_b, node_a])

    return DG

def digits(val):
    return int(re.sub("\D", "", val))

def format_key(key):
    key = key.strip() 
    if key.startswith('"') and key.endswith('"'):
        key = key[1:-1]
    return key 


def print_results(f, method, results):
    print (method)