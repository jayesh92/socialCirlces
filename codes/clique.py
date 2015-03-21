import os
import multiprocessing


class Cliques():
    '''
    Constructs max-cliques of various sizes over all test_egonets files
    '''
    def __init__(self):
        self.egonets='../egonets/'
        self.edge_set='./edges/'
        self.training_set='../Training/'
        self.testing_egonets='./test_egonets/'
        self.edge_set='./edges/'
        self.cliques='./cliques/'

    def find_cliques(self, file_index):
        filename=self.edge_set+str(file_index)+'.egonet.edges'
        out_file=self.cliques+str(file_index)+'.cliques'
        os.system('~/Desktop/graph_library/MaximalCliques/justTheCliques ' + filename + ' > ' + out_file + ' &')

    def find_all_cliques(self):
        for filename in os.listdir(self.testing_egonets):
            file_index=filename.split('.egonet')[0]
            self.find_cliques(file_index)

if __name__ == '__main__':
    clique = Cliques()
    clique.find_all_cliques()
