import os


class Construct():
    '''
    Constructs test_egonets
    Constructs edge set to give to clique finding algorithm
    '''
    def __init__(self):
        self.egonets='../egonets/'
        self.edge_set='./edges/'
        self.training_set='../Training/'
        self.testing_egonets='./test_egonets/'

    def construct_edge_set(self):
        for filename in os.listdir(self.egonets):
            out_file=open(self.edge_set+filename+'.edges','w')
            for line in file(self.egonets+filename):
                x=line.split(':')
                out_file.write(filename.split('.egonet')[0] + " " + x[0] + '\n')
                temp=x[1].split(' ')[1:]
                temp[-1]=temp[-1].strip('\n')
                if(len(temp)==1 and temp[0]==''):
                    continue
                for i in temp:
                    out_file.write(x[0] + " " + i + '\n')
            out_file.close()

    def construct_testing_egonets(self):
        for filename in os.listdir(self.egonets):
            file_index=filename.split('.egonet')[0]
            training_file=file_index+'.circles'
            if training_file not in os.listdir(self.training_set):
                os.system('cp ../egonets/' + file_index + '.egonet' + ' ./test_egonets/')

if __name__ == '__main__':
    construct = Construct()
    #construct.construct_testing_egonets()
    construct.construct_edge_set()
