#!/usr/bin/env python
# -*- coding: utf-8 -*-

# do not 

from graphviz import Digraph

graph_layout="dot"
filename="H003-10_bgcolor"

dot = Digraph(format="png")
dot.attr(layout=graph_layout)
dot.attr(bgcolor="darkgreen")

with dot.subgraph(name="cluster_X") as c:
    c.attr(bgcolor="cyan4")
    c.edge("C","D")

with dot.subgraph(name="cluster_Y") as c:
    c.attr(bgcolor="#26ffa2")
    c.edge("F","E")

with dot.subgraph(name="cluster_Z") as c:
    c.edge("G","H")

dot.edge("A","B")

print(dot)
dot.render(filename)
