import os
import numpy as np


class Graph():
    '''
    Constructs adjacency matrix
    Constructs adj_list from matrix and dumps it to adj_list
    Read method provided to read from adj_list file
    '''
    def __init__(self):
        self.egonets='../egonets/'
        self.adj_list_file='./adj_list'
        self.friend=np.zeros((28000,28000), dtype=bool)
        self.adj_list={}

        for filename in os.listdir(self.egonets):
            curr_node = int(filename.split('.egonet')[0])
            filename = self.egonets + filename
            for line in file(filename):
                x=line.split(':')
                first = int(x[0])
                self.friend[curr_node][first]= True
                self.friend[first][curr_node]= True
                rest = x[1].split(' ')[1:]
                rest[-1]=rest[-1].strip('\n')
                for nodes in rest:
                    if(nodes!=''):
                        node=int(nodes)
                        self.friend[first][node]=True
                        self.friend[node][first]=True

    def construct_adjacency_list(self):
        for i in range(len(self.friend)):
            connections=[]
            for j in range(len(self.friend[i])):
                if self.friend[i][j]:
                    connections.append(j)
            self.adj_list[i]=connections
        return self.adj_list

    def print_adjacency_list(self):
        f=open(self.adj_list_file, 'w')
        for i in range(len(self.friend)):
            f.write(str(i))
            for j in range(len(self.friend[i])):
                if self.friend[i][j]:
                    f.write(' ' + str(j)),
            f.write('\n')
        f.close()

    def read_adjacency_list(self):
        for line in file(self.adj_list_file):
            x=line.split(' ')
            x[-1]=x[-1].strip('\n')
            self.adj_list[x[0]] = x[1:]
        return self.adj_list

if __name__ == '__main__':
    graph=Graph()
    graph.read_adj_list()
