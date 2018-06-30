# -*- coding: utf-8 -*-
"""
Created on Mon Nov 06 15:36:06 2017

@author: siyuxie
"""
import re
def read_input(fname):
    
    with open(fname) as f:
        
        lines=f.readlines()
        nq=int(lines[0].strip())
        ns=int(lines[nq+1].strip())
        queries=[]
        for line in lines[1:nq+1]:
            line=line.strip()
            queries.append(line)          
        kb=[]

        for line in lines[nq+2:]:
            line=line.strip()
            kb.append(line)
            
        
        f.close()

    return nq,queries,ns,kb

def resolution(kb):
    answerlist=[]
    for q in queries:  
        global alpha
        print q
        if re.match(r'(^[\~])', q):
            alpha=q[1:]
            qq=q[1:]
        else:
            alpha='~'+q
            qq='~'+q
        global test
        test = 0
        answerlist.append(fol_resolution(kb,qq))
        
#        answerlist=fol_resolution(kb,q)
#        break
    
    return answerlist
        
def fol_resolution(kb,query):
    count_kb=0
    
    w=resolution_onestep(kb,query,count_kb)
    
    if w==1:
        return 1
#    elif test2==0:
#        return 0
    else:
        return 0
                
                    
        
def resolution_onestep(kb,query,count_kb):
    global test,test2
    test=0
#    test2=1
    print(query)
    print('in')
#    used=[]
    
    
    if alpha==query and count_kb>1:
#        test2=0
        return 0
        
    query_cut=query.split(' | ')
    for q in query_cut:
        if test==1: return 1
        
        part_q=re.findall(r'.+(?=\()',q)[0]
        var_q=re.findall(r'(?<=\()\S+(?=\))',q)[0].split(',')
        for sentence in kb:
            
            if test==1: return 1
            sentence_cut=sentence.split(' | ')
            sentence_remove=[]
            query_remove=[]
            theta=dict()
            new_theta=dict()
            flag=0
            resolvents=[]
            new_resolvents=''
            new_resolvent=[]                  
            for s in sentence_cut:
                print ('clauses_2line',sentence_cut)          
                part_s=re.findall(r'.+(?=\()',s)[0]
                if part_s=='~'+part_q or part_q=='~'+part_s:
                    print ('yes')
                    flag=1                    
                    var_s=re.findall(r'(?<=\()\S+(?=\))',s)[0].split(',')
                    for j in range(len(var_q)):
                        new_theta=unify(var_s[j],var_q[j],theta)
                        if new_theta==None:
                            flag=0
                            break
                    if new_theta==None:
                        flag=0                               
                        break

                            
                        
                if flag==0:
                    #print('zxc')
                    continue

                else:
                    sentence_remove.append(s)
                    query_remove.append(q)
                    count_kb+=1
#                    used.append(q)
#                    print ('used',used)
#                    kb=list(set(kb)-set(used))
#                    print ('kb',kb)
                    sentence_remain=list(set(sentence_cut)-set(sentence_remove))
                    query_remain=list(set(query_cut)-set(query_remove))
#                    if len(query_remain)==0 and len(sentence_remain)==0:
#                        test=1
                    if test==1:
                        return 1
                    
                    print ('new_theta',new_theta)    
                    for s_r in sentence_remain:
                        resolvents.append(s_r)
                    for q_r in query_remain:
                        resolvents.append(q_r)
#                print 'cl_cut',cl_cut,'clause_cut',clause_cut,'resolvents',resolvents                    
                    for resolvent in resolvents:
                        resolve=re.findall(r'(?<=\()\S+(?=\))',resolvent)[0].split(',')
                        print ('resolve',resolve)
                        c1=''
                        for r in resolve:
                            a1=re.findall(r'.+(?=\()',resolvent)[0]
                            if r in new_theta.keys() and re.match('[a-z]+$', r[0:1]):
                                r=new_theta[r]
                                c1=c1+r+','
                            else:
                                c1=c1+r+','
                            resolvent=a1+'('+c1+')'
                            resolvent=resolvent[:-2]+resolvent[-1]
                            print ('resolvent', resolvent)
                                      
                                
                        new_resolvent.append(resolvent)
                    new_resolvents=' | '.join(new_resolvent)
                    print (new_resolvents)
                    if new_resolvents=='':
                        test=1
                        return 1
                        #exit()
                        #return 1
                    else:
                        print ('iterate')
                        resolution_onestep(kb,new_resolvents,count_kb)
                        if test==1:
                            return 1
                        #print("12456")
                    
 
        
                
    return 0
                        
def unify(x,y,theta):
    if theta==None:
        return None
    elif x==y:
        return theta
    elif re.match('^[a-z]+$', x) and re.match('^[a-z]+$', y):        
        return None
    elif re.match('^[a-z]+$', x):
        return unify_var(x,y,theta)
    elif re.match('^[a-z]+$',y):
        return unify_var(y,x,theta)
    else:
        return None

def unify_var(var,x,theta):
    if var in theta.keys():
        return unify(theta[var],x,theta)
    elif x in theta.keys():
        return unify(var,theta[x],theta)
    else:
        theta[var]=x
        return theta
    
    
#def write_output(answerlist):
#     with open('output.txt','w') as fout:
#        for answer in answerlist:
#            if answer == 1:
#                print>>fout,'TRUE'
#            else:
#                print>>fout,'FALSE'
        
def main():
    
    global nq,ns,queries
#    test=0
    
    [nq,queries,ns,kb]=read_input('input4.txt')   
    answerlist=resolution(kb)
    for answer in answerlist:
        if answer==1:
            print ('true')
        else:
            print('false')
#    if answerlist==1:
#        print ('true')
#    else:
#        print('flase')
    print answerlist
#    write_output(answerlist)

    print ('done')


   


global test,alpha
test=0

            
if __name__ == "__main__":
    main()
