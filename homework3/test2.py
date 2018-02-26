# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 17:37:32 2017

@author: 69568
"""
import re
used=['H(x) | ~F(x)', '~H(x) | G(x)', '~C(John,Alice) | G(John)', '~C(John,Joe) | G(John)', '~B(x,y) | ~Q(y) | ~D(x,y) | G(x)', 'F(x) | ~G(x)', '~G(John)', 'H(Tom)', '~B(x,y) | ~C(x,y) | H(x)', 'F(x) | ~R(x)', '~R(John)', 'F(x) | ~A(x)', '~A(John)', '~Q(Alice) | H(John)', '~D(John,Joe) | H(John)', '~Q(Joe) | H(John)', '~H(Alice)', '~B(Alice,y) | ~Q(y) | ~D(Alice,y)', '~H(Joe)', '~B(Joe,y) | ~Q(y) | ~D(Joe,y)', '~B(John,Alice) | ~Q(Alice) | F(John)', '~D(x,Joe) | ~B(x,Joe) | F(x)', '~Q(Joe) | ~B(John,Joe) | F(John)', '~B(John,Alice) | ~Q(Alice)', '~D(John,Joe) | ~B(John,Joe)', '~Q(Joe) | ~B(John,Joe)']
clauses=['~R(John)', 'G(x) | ~F(x)', '~G(x) | H(x)', '~R(x) | H(x)', '~A(x) | H(x)', '~F(Alice)', '~F(Joe)', 'F(x) | ~H(x)', '~H(John)', 'G(Tom)', '~B(x,y) | ~C(x,y) | G(x)', '~C(John,Alice) | F(John)', '~C(John,Joe) | F(John)', '~B(x,y) | ~Q(y) | ~D(x,y) | F(x)', '~B(Alice,y) | ~C(Alice,y)', '~B(Joe,y) | ~C(Joe,y)', '~Q(Alice) | ~B(John,Alice) | H(John)', '~D(x,Joe) | ~B(x,Joe) | H(x)', '~Q(Joe) | ~B(John,Joe) | H(John)', '~C(John,Alice)', '~C(John,Joe)', '~B(John,y) | ~Q(y) | ~D(John,y)', '~Q(Alice) | A(John)', '~D(John,Joe) | A(John)', '~Q(Joe) | A(John)']
for s in used:
    if s in clauses:
        print 'in',s
print 'done'  





#if set(new).issubset(set(clauses)):
#    print 'in'
#else:
#    print 'not in'


#                clause4judge=[]
#                clause4judge=copy.deepcopy(clause_cut)
#                cl4judge=[]
#                cl4judge=copy.deepcopy(cl_cut)
#                
#                loop=0
#                for cl_judge in cl_cut:
##                    print 'cl_judge',cl_cut
#                    for clause_judge in clause_cut:
##                        print 'clause_judge',clause_cut
#                        if cl_judge=='~'+clause_judge or clause_judge=='~'+cl_judge:
##                            print 'remove'
#                            cl4judge.remove(cl_judge)
#                            clause4judge.remove(clause_judge)
#                if clause4judge==[] and cl4judge==[]:
#                    return 0
