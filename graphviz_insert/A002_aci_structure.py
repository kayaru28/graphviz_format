#!/usr/bin/env python
# -*- coding: utf-8 -*-
import data_prefectures
import csv
from graphviz import Digraph

COL_COMPORNENT  = 0
COL_ID          = 1
COL_NAME        = 2
global compornent
aci_id          = ""
label           = ""

KEY_CLUSTER = "CLUSTER"
KEY_NODE = "NODE"
KEY_EDGE = "EDGE"

global data
global row
global ROW_MAX


def updateData():
    global row
    global compornent
    global aci_id
    global label
    if(row<ROW_MAX):
        compornent  = data[row][COL_COMPORNENT]
        aci_id      = data[row][COL_ID]
        label       = data[row][COL_NAME]
        row = row + 1
        return True
    else:
        compornent  = ""
        aci_id      = ""
        label       = ""
        return False

def isUnderLayer(cluster_id):
    return len(aci_id)>len(cluster_id)

def isEdge():
    return compornent==KEY_EDGE

def isNotEdge():
    if isEdge():
        return False
    else:
        return True

def isNotEOF():
    if compornent == "" :
        return False
    else:
        return True

def create_subgraph(uplayer):
    print(aci_id)
    #print(label)
    name = 'cluster_' + label
    cluster_id = aci_id
    with uplayer.subgraph(name=name) as cluster:
        cluster.attr(label=label)
        cluster.node(name=label,label="",color="white",height = "0.001",width ="0.001")
        updateData()
        while (isUnderLayer(cluster_id) and isNotEdge() and isNotEOF()):
            if compornent == KEY_CLUSTER:
                create_subgraph(cluster)
            elif compornent == KEY_NODE:
                name = 'node_' + aci_id + label
                #print(name)
                cluster.node(name=name,label=label)
                updateData()

def create_edge(dot):
    print(isNotEOF())
    print(isEdge())
    while (isNotEOF() and isEdge()):
        source_node = aci_id
        dest_node   = label
        print(source_node + " -> " + dest_node)
        para_lhead  = 'cluster_' + dest_node
        para_ltail  = 'cluster_' + source_node
        dot.edge(source_node,dest_node,lhead=para_lhead,ltail=para_ltail)
        updateData()

                

if __name__ == "__main__":
    
    global data
    global row
    global ROW_MAX

    input_file_name = "A002_aci_structure_data.csv"
    with open(input_file_name) as f:
        #print(f.read())
        reader = csv.reader(f)
        data = [row for row in reader]

    ROW_MAX = len(data)
    row     = 0

    if updateData():
        dot = Digraph(format='png')
        dot.attr(compound="true")
        dot.attr(bgcolor="white")
        create_subgraph(dot)
        create_edge(dot)
        print(dot)
        dot.render("A002_aci_structure")








