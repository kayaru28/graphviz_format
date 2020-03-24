#!/usr/bin/env python
# -*- coding: utf-8 -*-

# do not 

from graphviz import Digraph

graph_layout="fdp"
filename="H003-02_K"

dot = Digraph(format="png")
dot1 = Digraph(format="png")
dot2 = Digraph(format="png")
dot.attr(layout=graph_layout)
dot1.attr(layout=graph_layout)
dot2.attr(layout=graph_layout)
#dot.attr(K="0.0")
dot1.attr(K="1.0")
dot2.attr(K="2.0")

for ni in range(3):
    name = "A"
    name2 = "A" + str(ni)
    dot.edge(name,name2)
    dot1.edge(name,name2)
    dot2.edge(name,name2)
    for nj in range(3):
        name = name2
        name2j = name + str(nj)
        dot.edge(name,name2j)
        dot1.edge(name,name2j)
        dot2.edge(name,name2j)
        for nk in range(3):
            name = name2j
            name2k = name + str(nk)
            dot.edge(name,name2k)
            dot1.edge(name,name2k)
            dot2.edge(name,name2k)



print(dot)
print(dot1)
print(dot2)
dot.render(filename+"-00")
dot1.render(filename+"-01")
dot2.render(filename+"-02")
