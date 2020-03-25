#!/usr/bin/env python
# -*- coding: utf-8 -*-

# do not 

from graphviz import Digraph

graph_layout="dot"
filename="H003-06-08_arrow"

dot = Digraph(format="png")
dot.attr(layout=graph_layout)

dot.edge("A","B",dir="both")
dot.edge("C","D",arrowhead="inv",dir="both")
dot.edge("E","F",arrowtail="inv",dir="both")
dot.edge("G","H",arrowtail="odot",arrowhead="tee",dir="both")
dot.edge("I","J",arrowtail="odot",arrowhead="tee",dir="both",arrowsize="2.0")


print(dot)
dot.render(filename)
