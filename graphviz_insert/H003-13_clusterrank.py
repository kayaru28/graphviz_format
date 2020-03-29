#!/usr/bin/env python
# -*- coding: utf-8 -*-

# do not 

from graphviz import Digraph

graph_layout="dot"
filename="H003-13_clusterrank"

dot = Digraph(format="png")
dot.attr(layout=graph_layout)
dot.attr(clusterrank="local")

with dot.subgraph(name="cluster_X") as c:
    c.edge("C","D")

with dot.subgraph(name="cluster_A") as d:
    with d.subgraph(name="cluster_Y") as c:
        c.edge("F","E")

    with d.subgraph(name="cluster_Z") as c:
        c.edge("G","H")

dot.edge("A","B")

print(dot)
dot.render(filename)

graph_layout="dot"
filename="H003-13-02_clusterrank"

dot = Digraph(format="png")
dot.attr(layout=graph_layout)
dot.attr(clusterrank="global")

with dot.subgraph(name="cluster_X") as c:
    c.edge("C","D")

with dot.subgraph(name="cluster_A") as d:
    with d.subgraph(name="cluster_Y") as c:
        c.edge("F","E")

    with d.subgraph(name="cluster_Z") as c:
        c.edge("G","H")

dot.edge("A","B")

print(dot)
dot.render(filename)


graph_layout="dot"
filename="H003-13-03_clusterrank"

dot = Digraph(format="png")
dot.attr(layout=graph_layout)
dot.attr(clusterrank="none")

with dot.subgraph(name="cluster_X") as c:
    c.edge("C","D")

with dot.subgraph(name="cluster_A") as d:
    with d.subgraph(name="cluster_Y") as c:
        c.edge("F","E")

    with d.subgraph(name="cluster_Z") as c:
        c.edge("G","H")

dot.edge("A","B")

print(dot)
dot.render(filename)

