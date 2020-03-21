#!/usr/bin/env python
# -*- coding: utf-8 -*-

from graphviz import Digraph


# formatはpngを指定(他にはPDF, PNG, SVGなどが指定可)
dot = Digraph(format='png')


dot.attr('node', shape='box')
dot.attr(compound='true')
#dot.attr(size='0.5,2.0!')
#dot.attr(newrank='true')
#dot.attr(layout='neato')

filename='H001_lambda_by_s3'

C_Lambda='cluster_A'
C_S3='cluster_B'

N_Lambda_Function='Lambda_Function'
N_S3_bucket='S3_bucket'
N_S3_nortification='bucket nortification'

L_lambda_function=N_Lambda_Function
L_S3_bucket=N_S3_bucket
L_lambda='Lambda_Function'
L_S3='S3_bucket'
L_S3_nortification=N_S3_nortification

with dot.subgraph(name=C_Lambda) as c:
    c.attr(label=L_lambda)
    c.node(name=N_Lambda_Function,label=L_lambda_function)

with dot.subgraph(name=C_S3) as c:
    c.attr(label=L_S3)
    c.node(name=N_S3_bucket,label=L_S3_bucket)
    c.node(name=N_S3_nortification,label=L_S3_nortification)    

dot.edge(N_Lambda_Function,N_S3_nortification,label='add permissions to access')
dot.edge(N_S3_bucket,N_S3_nortification,label='create bucket notification \nto Lambda Function', labelfloat='false')
print(dot)
dot.render(filename)
#ltail=`C_*`
#lhead=`C_*`
