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

global data
global row
global ROW_MAX


def updateData():
    global row
    global compornent
    global aci_id
    global label
    if(row < ROW_MAX):
        compornent  = data[row][COL_COMPORNENT]
        aci_id      = data[row][COL_ID]
        label       = data[row][COL_NAME]
        row = row + 1
        return True
    else:
        return False


def create_subgraph(uplayer):
    print(aci_id)
    #print(label)
    name = 'cluster_' + aci_id + label
    cluster_id = aci_id
    with uplayer.subgraph(name=name) as cluster:
        cluster.attr(label=label)
        cluster.node(name=label,label=label)
        updateData()
        while (row < ROW_MAX and len(aci_id)>len(cluster_id)):
            if compornent == KEY_CLUSTER:
                create_subgraph(cluster)
            elif compornent == KEY_NODE:
                name = 'node_' + aci_id + label
                #print(name)
                cluster.node(name=name,label=label)
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
        create_subgraph(dot)
        print(dot)
        dot.render("A002_aci_structure")








