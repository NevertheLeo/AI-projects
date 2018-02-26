# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 22:52:47 2017

@author: 69568
"""
import re

   
    
theta={}
theta['y']='Joy'
pp='May(y,Billy)','Mother(liz,y)'
for p in pp:
    p_cut=re.findall(r'(?<=\()\S+(?=\))',p)[0].split(',')
    c1=''
    for r in p_cut:
        a1=re.findall(r'.+(?=\()',p)[0]
    
        if r in theta.keys() and re.match('[a-z]+$', r[0:1]):
            r=theta[r]
#            print 'r1',r
            c1=c1+r+','
#            print 'a',a1
        else:
#            print 'r2',r
            c1=c1+r+','
#            print 'c',c1
        p=a1+'('+c1+')'
        p=p[:-2]+p[-1]
     
            
    print p
    


