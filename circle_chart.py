#!/usr/bin/env python
# -*- coding: utf-8 -*-
from graphviz import Digraph


dot = Digraph(format='png')
filename = "circle"
dot_layout = "neato" # dot……階層状配置/neato……等間隔配置/twopi……放射状配置/circo…環状配置

dot.attr('node', shape='oval')
#dot.attr(size='0.5,2.0!')
dot.attr(newrank="true")
dot.attr(layout=dot_layout)
dot.node(name="A")
dot.node(name="B1")
dot.node(name="B2")
dot.node(name="B3")
dot.node(name="B4")
dot.node(name="B5")
dot.node(name="B6")
dot.node(name="C1")
dot.node(name="C2")
dot.node(name="C3")
dot.node(name="C4")
dot.node(name="C5")
dot.node(name="C6")
length1="1.0"
length2="2.0"
dot.edge("A","B1",len=length1)
dot.edge("A","B2",len=length1)
dot.edge("A","B3",len=length1)
dot.edge("A","B4",len=length1)
dot.edge("A","B5",len=length1)
dot.edge("A","B6",len=length1)
dot.edge("A","C1",len=length2)
dot.edge("A","C2",len=length2)
dot.edge("A","C3",len=length2)
dot.edge("A","C4",len=length2)
dot.edge("A","C5",len=length2)
dot.edge("A","C6",len=length2)

print(dot)
dot.render(filename)