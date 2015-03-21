import operator
from graph import Graph


class ExtendClique():
    '''
    Takes in a clique and extends it iteratively,
    till the score is more than threshold
    '''
    def __init__(self):
        self.threshold_score=0.4
        self.adj_list = Graph().read_adjacency_list()

    def extend(self, clique, nodes):
        # @param clique, list of nodes in the current clique
        # @param nodes, list of nodes
        # @return maximal clique above threshold
        clique_size = len(clique)
        degree_num = clique_size*(clique_size-1.0)
        for vertex in clique:
            nodes.remove(vertex)
        while True:
            d={}
            nums={}
            max_benefit=0.0
            for node in nodes:
                increment=0
                for vertex in clique:
                    if node in self.adj_list[vertex]:
                        increment+=1
                score_num=degree_num+(2*increment)
                score_den=(clique_size+1)*clique_size
                d[node]=(score_num*1.0)/(score_den*1.0)
                nums[node]=2*increment
                max_benefit=max(max_benefit, d[node])
            
            for key,value in d.items():
                if value==max_benefit:
                    degree_num+=nums[key]
                    clique_size+=1

            score = (degree_num*1.0)/(clique_size*(clique_size-1.0)*1.0)

            if score <= self.threshold_score:
                break
            else:
                for key,value in d.items():
                    if value==max_benefit:
                        clique.append(key)
                        nodes.remove(key)
        return clique

if __name__ == '__main__':
    extendClique = ExtendClique()
    clique=[0, 3, 17, 22, 80, 101, 103, 118, 157, 169, 185, 188, 213, 223, 228]
    clique=map(lambda x: str(x), clique)
    nodes=map(lambda x: str(x),range(239))
    print extendClique.extend(clique,nodes)
    print len(clique)
