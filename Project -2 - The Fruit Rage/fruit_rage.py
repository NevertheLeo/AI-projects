# -*- coding: utf-8 -*-
"""
Spyder Editor


"""
import numpy as np
import time
import math


        

def read_input(fname):
    
    with open(fname) as f:
        n=int(f.readline().strip())
        p=int(f.readline().strip())
        remain_time=float(f.readline().strip())
        board=[[]for i in range(n)]

        i=0
        for line in f.readlines():
            line=line.strip()
            for s in line:
                board[i].append(s)           
            i+=1
            
        f.close()

    return n,p,remain_time,board

def search_graph(board):
    
    graphicslist=[]
    node2graphics=np.zeros((n,n),dtype=np.int32)
    graphics_index=set([]);
    if board[0][0]!='*':        
        graphics=[(0,0)]
        graphicslist.append(graphics)
        node2graphics[0][0]=1
        graphics_index.add(node2graphics[0][0])

   #first row 
    for i in range(1,n):
        if board[0][i]!='*':
            if board[0][i]==board[0][i-1]:
                graphicslist[node2graphics[0][i-1]-1].append((0,i))
                node2graphics[0][i]=node2graphics[0][i-1]

            else:
                tempgraphics=[(0,i)]
                graphicslist.append(tempgraphics)
                node2graphics[0][i]=len(graphicslist)
                graphics_index.add(node2graphics[0][i])
    
    #first column
    for j in range(1,n):
        if board[j][0]!='*':
            if board[j][0]==board[j-1][0]:
                graphicslist[node2graphics[j-1][0]-1].append((j,0))
                node2graphics[j][0]=node2graphics[j-1][0]

            else:
                tempgraphics=[(j,0)]
                graphicslist.append(tempgraphics)
                node2graphics[j][0]=len(graphicslist)
                graphics_index.add(node2graphics[j][0])
    #others:
    for i in range(1,n):
        for j in range(1,n):
            if board[i][j]!='*':
                if board[i][j]==board[i][j-1]:
                    graphicslist[node2graphics[i][j-1]-1].append((i,j))
                    node2graphics[i][j]=node2graphics[i][j-1]
                    if board[i][j]==board[i-1][j]: 
                        if node2graphics[i][j]==node2graphics[i-1][j]:
                            continue
                        graphicslist[node2graphics[i-1][j]-1]= list(set(graphicslist[node2graphics[i-1][j]-1]).union(set(graphicslist[node2graphics[i][j]-1])))
                        temp_value=node2graphics[i][j]-1                        
                        for (temp_i,temp_j) in graphicslist[temp_value]:
                            node2graphics[temp_i][temp_j]=node2graphics[i-1][j]
                        graphics_index.discard(temp_value+1)
                else:
                    if board[i][j]==board[i-1][j]:
                        graphicslist[node2graphics[i-1][j]-1].append((i,j))
                        node2graphics[i][j]=node2graphics[i-1][j]
                    else:
                        tempgraphics=[(i,j)]
                        graphicslist.append(tempgraphics)
                        node2graphics[i][j]=len(graphicslist)
                        graphics_index.add(node2graphics[i][j])


    graphics_after=[]
    max_len=-1
    max_graphics=None
    for i in graphics_index:
        graphics_after.append(graphicslist[i-1])
        if max_len< len(graphicslist[i-1]):
            max_len=len(graphicslist[i-1])
            max_graphics=graphics_after[len(graphics_after)-1]
    

        
    graphics_after.remove(max_graphics)
    graphics_after.insert(0,max_graphics)  
    


    return graphics_after,max_len      






def drop_down(graphics,board):
    def getKey1(choice_rand):
        return choice_rand[0]   
    graphics_row=sorted(graphics,key=getKey1,reverse=True)
    def getKey2(choice_row):
        return choice_row[1]   
    graphics=sorted(graphics_row,key=getKey2)
    
    newboard=[[0 for col in range(n)] for row in range(n)]

    previous_j=-1
    for i in range(n):
        for j in range(n):
            newboard[i][j]=board[i][j]
    

    
    for i,j in graphics:

        newboard[i][j]='*'  
    
    
    for i,j in graphics:
        if j==previous_j:
            continue
        else:
            previous_j=j
            i_value=i
            for ii in range(i,-1,-1):
                if newboard[ii][j]=='*':
                    continue
                else:
                    
                    newboard[i_value][j]=newboard[ii][j]
                    newboard[ii][j]='*'
                    i_value=i_value-1
    

    return newboard,i,j
                    
    
def start_graph(board):
    alpha=float("-inf")
    beta=float("inf")
    depth=1
    value=0 

    [graphics_after,max_len]=search_graph(board)

    length=float(len(graphics_after))
    print length
   
    if length==1:
        for i,j in graphics_after[0]:
            board[i][j]='*'
        return board,i,j
    if depth==1:
        [noboard,i,j]=drop_down(graphics_after[0],board)
        
    current_time=time.time()    
    everagetime=remain_time/length
    onesteptime=current_time-start_time
    print onesteptime

    if onesteptime==0:
        end_depth=3
    else:
        end_depth=int(math.log(everagetime/onesteptime,length))
    
    
    if end_depth==0:
        end_depth=1
        
    print end_depth
    if depth==end_depth:
        return drop_down(graphics_after[0],board)

    
    max_graphics=None   
    for graphics in graphics_after: 
        if time.time()-start_time+everagetime>remain_time:

            return drop_down(graphics_after[0],board)

        [new_board,new_i,new_j]=drop_down(graphics,board)    

        temp_alpha=min_graph(new_board,alpha,beta,depth+1,value+len(graphics)^2,end_depth)

        if temp_alpha>alpha:
            alpha=temp_alpha
            max_graphics=graphics
        print max_graphics,alpha
    return drop_down(max_graphics,board)
        
    
    
        
def max_graph(board,alpha,beta,depth,value,end_depth):
    [graphics_after,max_len]=search_graph(board)

    if len(graphics_after)==1:
        return value+(len(graphics_after[0]))^2
    
    if depth==end_depth:
        value=value+max_len^2

        return value

        
    for graphics in graphics_after:
#        print 'maxgraphics',graphics
        [new_board,new_i,new_j]=drop_down(graphics,board)
        alpha=max(alpha,min_graph(new_board,alpha,beta,depth+1,value+len(graphics)^2,end_depth))
        
        if alpha >= beta:
            return beta
    return alpha
        
        
def min_graph(board,alpha,beta,depth,value,end_depth):

    [graphics_after,max_len]=search_graph(board)


    if len(graphics_after)==1:

        return value-(len(graphics_after[0]))^2
    
    if depth==end_depth:

        value=value-max_len^2
        return value

    for graphics in graphics_after:
#        print 'mingraphics',graphics
        [new_board,new_i,new_j]=drop_down(graphics,board)
        beta=min(beta,max_graph(new_board,alpha,beta,depth+1,value-len(graphics)^2,end_depth))
        
        if beta <= alpha:
            return alpha
    return beta
            

def write_output(board,i,j):
       
    with open('output.txt','w') as fout:
        print>>fout,chr(j+65)+str(i+1)
        for m in range(n):
            txt=''
            for fruit in board[m]:
                txt+=str(fruit)
            print>>fout,txt
    

    
    
    
    
    
    

                    
            
            

def main():
    global start_time,remain_time
    start_time=time.time()
    global n
    [n,p,remain_time,ini_board]=read_input('input.txt')
    [final_board,final_i,final_j]=start_graph(ini_board)


    write_output(final_board,final_i,final_j)





    
            
if __name__ == "__main__":
    main()
