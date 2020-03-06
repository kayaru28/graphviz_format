#!/usr/bin/env python
# -*- coding: utf-8 -*-

from graphviz import Digraph


# formatはpngを指定(他にはPDF, PNG, SVGなどが指定可)
dot = Digraph(format='png')


dot.attr('node', shape='box')
#dot.attr(size='0.5,2.0!')
dot.attr(newrank="true")
dot.attr(layout="neato")
with dot.subgraph(name='clusterA') as clusterA:
    clusterA.attr(label='SwitchA')
    clusterA.node_attr={'width':'0.5','height':'0.5'}
    clusterA_left = 10
    clusterA_right = 12
    clusterA_top = 10
    clusterA_bottom = 15
    
    clusterA.node(name="A_LB",label="A",pos="10,10!")
    clusterA.node(name="B_LB",label="B",pos="10,15!")
    clusterA.node(name="C_LB",label="C",pos="12,10!")
    clusterA.node(name="D_LB",label="D",pos="12,15!")
with dot.subgraph(name='clusterA') as clusterB:
    clusterB.attr(label='SwitchB')
    clusterB.node_attr={'width':'0.5','height':'0.5'}
    clusterB.node(name="BA_LB",label="A",pos="10,11!")
    clusterB.node(name="BB_LB",label="B",pos="10,16!")
    clusterB.node(name="BC_LB",label="C",pos="12,11!")
    clusterB.node(name="BD_LB",label="D",pos="12,16!")

print(dot)
dot.render("tutorial")