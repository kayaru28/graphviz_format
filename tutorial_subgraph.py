#!/usr/bin/env python
# -*- coding: utf-8 -*-

from graphviz import Digraph


# formatはpngを指定(他にはPDF, PNG, SVGなどが指定可)
dot = Digraph(format='png')


dot.attr('node', shape='box')
#dot.attr(size='0.5,2.0!')
dot.attr(newrank="true")
dot.attr(layout="neato")
clusterA = dot.subgraph(name='clusterA')
dot.subgraph(name='clusterA').attr(label='SwitchA')
dot.subgraph(name='clusterA').node_attr={'width':'0.5','height':'0.5'}
dot.subgraph(name='clusterA').node(name="A_LB",label="A",pos="10,10!")
dot.subgraph(name='clusterA').node(name="B_LB",label="B",pos="10,15!")
with dot.subgraph(name='clusterA') as clusterB:
    clusterB.attr(label='SwitchB')
    clusterB.node_attr={'width':'0.5','height':'0.5'}
    clusterB.node(name="BA_LB",label="A",pos="10,11!")
    clusterB.node(name="BB_LB",label="B",pos="10,16!")
    clusterB.node(name="BC_LB",label="C",pos="12,11!")
    clusterB.node(name="BD_LB",label="D",pos="12,16!")

print(dot)
dot.render("tutorial")