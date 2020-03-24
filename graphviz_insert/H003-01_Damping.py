#!/usr/bin/env python
# -*- coding: utf-8 -*-

# do not 

from graphviz import Digraph

dot = Digraph(format="png")
dot1 = Digraph(format="png")
dot2 = Digraph(format="png")
dot.attr(layout="neato")
dot1.attr(layout="neato")
dot2.attr(layout="neato")
dot.attr(Damping="0.0")
dot1.attr(Damping="5.0")
dot2.attr(Damping="100.0")

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
            for nl in range(3):
                name = name2k
                name2l = name + str(nl)
                dot.edge(name,name2l)
                dot1.edge(name,name2l)
                dot2.edge(name,name2l)




filename="H003-01_Damping"

print(dot)
print(dot1)
print(dot2)
dot.render(filename+"-00")
dot1.render(filename+"-01")
dot2.render(filename+"-02")
