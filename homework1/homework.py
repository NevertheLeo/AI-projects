# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 14:17:39 2017

@author: 69568
"""
import random
import bisect
import math
import copy
import numpy as np 
from scipy.sparse import coo_matrix
import sys   

sys.setrecursionlimit(1000000)

#read input, get n,p and find where the tree is
def read_input(fname):
    
    with open(fname) as f:
        string=f.readline().strip()
        n=f.readline().strip()
        n=int(n)
        p=f.readline().strip()
        p=int(p)
#        state=[[0 for i in range(n)] for i in range(n)]
        row=[]
        col=[]
        data=[]
#        state_row=np.array(row,dtype=np.uint32)
#        state_col=np.array(col,dtype=np.uint32)
#        state_data=np.array(data,dtype=np.uint32)
        i=0
        for line in f.readlines():
            line=line.strip()
            j=0
            for s in line:
                if s=='2':
                    row.append(i)
                    col.append(j)
                    data.append(2)
#                    state[i][j]=2
                j+=1                
            i+=1
            
        f.close()
#    print 'state_row,state_col,state_data',state_row,state_col,state_data
    return string,n,p,row,col,data#state_row,state_col,state_data
  
#==============================================================================
# DFS    
#==============================================================================
def DFS_output(state,p):
    if DFS_iter(state,0,p)==1:        
        with open('output.txt','w') as fout:
            print>>fout,'OK'

            for i in range(n):
                txt=''
                for lizard in state[i]:
                    txt+=str(lizard)
                    
                print>>fout,txt
    else:
        with open('output.txt','w') as fout:
           print>>fout,'FAIL','\n'
        
    
    
    
    
def DFS_iter(state,i,p):
    if p==0:
        return 1
    if i==n:
        return 0
    return DFS_row(state,i,p,0)    

    
    
def DFS_row(state,i,p,start):
    if p==0:
        return 1
    tree_col=-1
    col=start
    for tree in state[i][start:]:
        if tree==2:
            tree_col=col
            break
        col+=1
    if (tree_col==-1)|(tree_col==n-1):
        j=start
        end=n-1
        if tree_col==-1:
            end=n
        for lizard in state[i][start:end]:
            
            state[i][j]=1
            if not_conflict(state,i,j)==1:
                if DFS_iter(state,i+1,p-1)==1:
                    return 1
            state[i][j]=0
            j+=1
        if DFS_iter(state,i+1,p)==1:
            return 1
            
    else:        
        j=start
        if state[i][j]==2:
            return DFS_row(state,i,p,tree_col+1)
              

        for lizard in state[i][start:tree_col]:
            state[i][j]=1
            if not_conflict(state,i,j)==1:
                if DFS_row(state,i,p-1,tree_col+1)==1:
                    
                    return 1
            state[i][j]=0
            j+=1
        if DFS_row(state,i,p,tree_col+1)==1:
            return 1           
    return 0
            
           
#==============================================================================
# BFS    
#==============================================================================

def BFS_output(state_row,state_col,state_data):
    state=coo_matrix((state_data, (state_row, state_col)), shape=(n, n)).toarray()
    with open('output.txt','w') as fout:
        print>>fout,'OK'
        print>>fout,state
        
        
#        for lizard in state:
#            txt=''        
#            for li in lizard:
#                txt+=str(li)
#            print>>fout,txt
    

def BFS(state_row,state_col,state_data,p):
    pp=p
    #convert current state into a sparse matrix 
    current_info=list()
    whole_state=list()
    i=0
    current_info.append(p)
    current_info.append(i)
    current_info.append(state_row)
    current_info.append(state_col)
    current_info.append(state_data)
    whole_state.append(current_info)
      
    has_result=0
    while(len(whole_state)!=0):
        sta=whole_state.pop(0)
#        print'pop_sta',sta[0]
        current_p=sta[0]        
        if current_p==0:
            has_result=1
            BFS_output(sta[2],sta[3],sta[4])
#            print 'Done'
            break
        BFS_row(whole_state,sta,0,pp)
#        print 'whole_state',whole_state
#        print'sta2',sta
    if has_result==0:
        with open('output.txt','w') as fout:
           print>>fout,'FAIL','\n' 

def BFS_row(whole_state,sta,start,pp):

#    print'sta',sta
    tree_col=-1
    col=start
    p=sta[0]
    i=sta[1]  
    
    state_row=[0 for h in range(pp+len(sta[2]))]
    state_col=[0 for g in range(pp+len(sta[3]))]
    state_data=[0 for j in range(pp+len(sta[4]))]
#    print state_row,state_col,state_data
#    state_row=sta[2]
#    state_col=sta[3]
#    state_data=sta[4]


    if p==0:
        return
    if i==n:
        return
    
    state=coo_matrix((sta[4], (sta[2], sta[3])),dtype=np.uint32,shape=(n, n)).toarray()
    
#    print state
    for tree in state[i][start:]:
        if tree==2:
            tree_col=col
            break
        col+=1
    if (tree_col==-1)|(tree_col==n-1):
        j=start
        end=n-1
        if tree_col==-1:
            end=n
        len_row=len(sta[2])       
        len_col=len(sta[3])
        len_data=len(sta[4])
        
        for lizard in state[i][start:end]:            
            state[i][j]=1
#            state.
#            print 'state[i][j]',state
            if not_conflict(state,i,j)==1:
                
                current_info=list()
                current_info.append(p-1)
                current_info.append(i+1)
                
                state_row[len_row]=i          
                current_info.append(state_row)
                
                state_col[len_col]=j
                current_info.append(state_col)
                
                
                state_data[len_data]=1
                current_info.append(state_data)
                print 'current_info',current_info
#                wholestate=copy.deepcopy(whole_state)
                whole_state.append(current_info)
                print whole_state

#            print 'wholestate',wholestate    
            state[i][j]=0
#            print'state[i][j]=0',state
            j+=1
#        print 'wholestate',wholestate   
        
        #if conflict:    
        current_info=list()
        current_info.append(p)
        current_info.append(i+1)              
        current_info.append(state_row)
        current_info.append(state_col)
        current_info.append(state_data)
        whole_state.append(current_info)
#        print 'wholestate_new',whole_state,whole_state.pop(0)
        

    else:        
        j=start
        if state[i][j]==2:
            BFS_row(whole_state,sta,tree_col+1)
              

        for lizard in state[i][start:tree_col]:
            state[i][j]=1
            if not_conflict(state,i,j)==1:
                sta[2].append(i)
                sta[3].append(j)
                sta[4].append(1)#[i][j]=1
                sta[0]-=1
                BFS_row(whole_state,sta,tree_col+1)
                sta[0]+=1
            sta[2].append(state_row)
            sta[3].append(state_col)
            sta[4].append(state_data)#[i][j]=0
                
            j+=1
        BFS_row(whole_state,sta,tree_col+1,pp)         
    

#==============================================================================
# SA
#==============================================================================


def SA_randomlizards(state,p):
    

    j_index=[0 for k in range(n*n)]
    count=0
    start=[0 for k in range(n)]
    for i in range(n):
        j=0
        start[i]=count
        for tree in state[i]:
            if tree!=2:
                j_index[count]=j                
                count+=1
            j+=1
                           

    random_p=random.sample(range(count),p)
#    print random_p
    
    lizard_pos=[[0 for m in range(2)] for l in range(p) ]
    k=0
    for rand in random_p:
        i=bisect.bisect_right(start,rand)-1
        j=j_index[rand]
#        print i,j,rand
        state[i][j]=1
        lizard_pos[k][0]=i
        lizard_pos[k][1]=j
        k+=1
#        print lizard_pos
    return state,lizard_pos


            
            
# count the num of conflict lizards
def num_conflict(state,i,j) :
#    print 'i',i
    count_conflict = 0  
    #same column <i state[i-k,j] for k=[1->i]    
    for k in range(i):
        if state[i-k-1][j]==1:
            count_conflict+=1
        elif state[i-k-1][j]==2:
            break
        
    #same column >i state[i+k,j] for k=[1->n-i-1]  
    for k in range(n-i-1):
        if state[i+k+1][j]==1:
            count_conflict+=1
        elif state[i+k+1][j]==2:
            break
        
    #left-up diagonol <i state[i-k,j-k] for k=[1->min(i,j)]  
    for k in range(min(i,j)):
        if state[i-k-1][j-k-1]==1:
            count_conflict+=1
        elif state[i-k-1][j-k-1]==2:
            break
        
    #right-down diagonol >i state[i+k,j+k] for k=[1->min(n-1-i,n-1-j)]
    for k in range(min(n-i-1,n-j-1)):
        if state[i+k+1][j+k+1]==1:
            count_conflict+=1
        elif state[i+k+1][j+k+1]==2:
            break
        
    #right-up diagonol <i state[i-k,j+k] for k=[1->min(i,n-1-j)]
    for k in range(min(i,n-j-1)):
        if state[i-k-1][j+k+1]==1:
            count_conflict+=1
        elif state[i-k-1][j+k+1]==2:
            break
        
    #left-down diagonol >i state[i+k,j-k] for k=[1->min(j,n-1-i)] 
    for k in range(min(j,n-i-1)):
        if state[i+k+1][j-k-1]==1:
            count_conflict+=1
        elif state[i+k+1][j-k-1]==2:
            break
    #same row state[i][j-k] for k=[1->j]
    for k in range(j):
        if state[i][j-k-1]==1:
            count_conflict+=1
        elif state[i][j-k-1]==2:
            break
    #same row state[i][j+k] for k=[1->n-1-j]
    for k in range(n-1-j):
        if state[i][j+k+1]==1:
            count_conflict+=1
        elif state[i][j+k+1]==2:
            break
    return count_conflict
                
def total_conflict(lizard,state):
    all_conflict=0
#    print 'lizard',lizard
    for li in lizard:
        i=li[0]
        j=li[1]
        all_conflict+=num_conflict(state,i,j)

    return all_conflict



def randselect_nextpos(state,i,j):
    #print "before: i,j ",i,j
    #new_state=[[0 for q in range(n)] for w in range(n)]
    possible_next=[[0 for y in range(2)] for x in range(8)]
    loweri=max(0,i-1)
    lowerj=max(0,j-1)
    upperi=min(i+1,n-1)
    upperj=min(j+1,n-1)
    index=0
    for m in range(loweri,upperi+1):
        for k in range(lowerj,upperj+1):
            if(m==i& k==j):
                continue
            if state[m][k]==0:                
                possible_next[index][0]=m
                possible_next[index][1]=k
                index+=1
    if index==0:
        #print "No Found next stop"
        return i,j            
    #print 'index',index
    rand_next=random.randrange(index)
    #print 'rand_next',rand_next
#    print possible_next[rand_next]
    new_i=possible_next[rand_next][0]
    new_j=possible_next[rand_next][1]
    #print "after: i,j ",new_i,new_j,i,j
    state[new_i][new_j]=1
    state[i][j]=0
    
    #print 'new_state:',state
    return new_i,new_j
    
    
    
def SA_Search(state,p):
    
    [state,lizard_pos]=SA_randomlizards(state,p)
    #print 'lizard_pos',lizard_pos
#    print lizard_pos
    temperature = 10000
    while (temperature > 0.00001) :
        random_lizard_index=random.randrange(0,p)
        i=lizard_pos[random_lizard_index][0]
        j=lizard_pos[random_lizard_index][1]
        #print'randi,j',i,j,random_lizard_index
        current_conflict=total_conflict(lizard_pos,state)
        #print'current_conflict',current_conflict
        [new_i,new_j]=randselect_nextpos(state,i,j)
        #print 'newi,newj',new_i,new_j
        #print "i,j before nextstop",i,j,"lizard_pos",lizard_pos
        lizard_pos[random_lizard_index][0]=new_i
        lizard_pos[random_lizard_index][1]=new_j
        #print "i,j after nextstop",new_i,new_j,"lizard_pos",lizard_pos
        #print 'newlizard_pos',lizard_pos
        next_conflict=total_conflict(lizard_pos,state)
        #print'totalconflict',next_conflict
        E=next_conflict-current_conflict
        better=0
        if E<0:
            better=1
        elif math.exp((-1)*E/temperature) > random.random():
            better=1
        if better==0:
            state[new_i][new_j]=0
            state[i][j]=1
            lizard_pos[random_lizard_index][0]=i
            lizard_pos[random_lizard_index][1]=j
#            print "better==0"
            #print new_i,new_j,i,j
        #print'current_state',state
        if next_conflict==0:
            return state
        temperature *= 0.99999;
        

def SA_output(state):
    with open('output.txt','w') as fout:
        if state==None:
            print>>fout,'FAIL','\n'
        else:
            print>>fout,'OK'
            for lizard in state:
                txt=''        
                for li in lizard:
                    txt+=str(li)
                print>>fout,txt
          
            
def not_conflict(state,i,j):
    
    for k in range(i):
        if state[i-k-1][j]==1:
            return 0
        elif state[i-k-1][j]==2:
            break
        
    for k in range(min(i,j)):
        if state[i-k-1][j-k-1]==1:
            return 0
        elif state[i-k-1][j-k-1]==2:
            break
    for k in range(min(i,n-j-1)):
        if state[i-k-1][j+k+1]==1:
            return 0
        elif state[i][j]==2:
            break
    return 1
    
    

def main():
    global n
    [al,n,p,state_row,state_col,state_data]=read_input('input.txt')

#    if al=='DFS':
#        DFS_output(state,p)
#        print'done'
#    el
    if al=='BFS':
        BFS(state_row,state_col,state_data,p)
#    elif al=='SA':
#       randselect_nextpos(state,p)
#        state=SA_Search(state,p)
#        SA_output(state)
#        print'done'

    else:
        with open('output.txt','w') as fout:
           print>>fout,'FAIL','\n' 


    
            
if __name__ == "__main__":
    main()
