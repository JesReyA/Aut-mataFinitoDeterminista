#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 20:27:45 2026

@author: erikazr
"""

import graphviz

if __name__ == "__main__":  
    dot = graphviz.Digraph(comment = "validacion de correos", format ='png')
    dot.attr(rankdir = 'LR')
    
    dot.attr('node', shape='doublecircle')
    dot.node('q0')

# Estado impar (círculo simple)
    dot.attr('node', shape='circle')
    dot.node('q1')
    
    dot.edge('q0', 'q1', label='alo')
    #renderiza la imagen
    dot.render('mi_automata', view=True)