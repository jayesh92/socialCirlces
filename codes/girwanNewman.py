import os
import snap
from graph import Graph


class GirwanNewman():
    def __init__(self):
        self.adj_list=Graph().read_adjacency_list()

    def compute(self):
        for filename in os.listdir('./test_egonets'):
            index=filename.split('.egonet')[0]
            new_file='./edges/'+index+'.egonet.edges'
            
            G = snap.TUNGraph.New()
            G.AddNode(int(index))
            for node in self.adj_list[index]:
                G.AddNode(int(node))

            for line in file(new_file):
                line=line.strip('\n')
                x=line.split(' ')
                x=map(lambda x: int(x), x)
                if not G.IsEdge(x[1], x[0]):
                    G.AddEdge(x[0], x[1])
            
            print 'Computing for ' + index

            CmtyV = snap.TCnComV()
            modularity = snap.CommunityGirvanNewman(G, CmtyV)

            for Cmty in CmtyV:
                for NI in Cmty:
                    print NI,
                print

            G.Clr()

if __name__ == '__main__':
    GirwanNewman().compute()

