#!/usr/bin/env python
# -*- coding: utf-8 -*-
import data_prefectures
from graphviz import Digraph

if __name__ == "__main__":
    prefectures= data_prefectures.prefectures()
    # print(prefectures.data)
    # print(prefectures.get_number("東京都"))

    print('対象の都道府県を入力してください')
    prefecture_name = input('>> ')
    prefecture_code = prefectures.get_code(prefecture_name)

    if prefecture_code == prefectures.ERROR_CODE:
        print("no exist prefecture")
    else:
        filename = "A001_prefecture_circle"
        dot_layout = "neato" # dot……階層状配置/neato……等間隔配置/twopi……放射状配置/circo…環状配置


        dot = Digraph(format='png')
        dot.attr(layout=dot_layout)
    
        for code in range(47):
            if prefecture_code != code:
                distance = str(prefectures.get_standerdized_distance(prefecture_code,code))
                name = prefectures.get_name(code)
                dot.edge(prefecture_name,name,len=distance)

        print(dot)
        dot.render(filename)






