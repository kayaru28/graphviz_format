#!/usr/bin/env python
# -*- coding: utf-8 -*-

# do not 

from graphviz import Digraph

graph_layout="dot"
filename="H003-18_concentrate_true"
dot = Digraph(format="png")
dot.attr(layout=graph_layout)
dot.attr(concentrate="true")
dot.edge("A","C")
dot.edge("C","A")
dot.edge("A","D")

print(dot)
dot.render(filename)

graph_layout="dot"
filename="H003-18_concentrate_false"
dot = Digraph(format="png")
dot.attr(layout=graph_layout)
dot.attr(concentrate="false")
dot.edge("A","C")
dot.edge("C","A")
dot.edge("A","D")

print(dot)
dot.render(filename)


