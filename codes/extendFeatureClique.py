import os
import operator
from graph import Graph
from features import Feature


class ExtendFeatureClique():
    '''
    Takes in a clique and extends it iteratively,
    by adding vertices as per best feature heuristic
    till the score is more than threshold
    '''
    def __init__(self):
        self.threshold_score=1.0
        self.size_threshold=20
        self.k=57
        self.top_10_cliques='./top_cliques/'
        self.adj_list = Graph().read_adjacency_list()
        self.feature_vector=Feature().read_features()
        self.topk_features=Feature().read_topk_features(self.k)

    def extend(self, clique, index):
        # @param clique, list of nodes in the current clique
        # @param nodes, list of nodes
        # @return maximal clique above threshold
        clique_size = len(clique)
        degree_num = clique_size*(clique_size-1.0)
        nodes = self.adj_list[index][:]
        nodes[-1]=nodes[-1].strip('\n')
        clique[-1]=clique[-1].strip('\n')
        for vertex in clique:
            if vertex in nodes:
                nodes.remove(vertex)
        while True:
            if len(nodes)==0:
                break
            d={}
            nums={}
            max_benefit=0.0
            for node in nodes:
                increment=0
                score=0.0
                max_score = (reduce(lambda x,y: x+y, self.topk_features.values()))*clique_size*1.0
                for vertex in clique:
                    for key,value in self.topk_features.items():
                        if key in self.feature_vector[node] and key in self.feature_vector[vertex]:
                            if self.feature_vector[node][key] == self.feature_vector[vertex][key]:
                                score+=value
                    if node in self.adj_list[vertex]:
                        increment+=1
                d[node]=(score*1.0)
                nums[node]=2*increment
                max_benefit=max(max_benefit, d[node])
            
            for key,value in d.items():
                if value==max_benefit:
                    degree_num+=nums[key]
                    clique_size+=1
            
            degree_score = (degree_num*1.0)/(clique_size*(clique_size-1.0)*1.0)

            if clique_size>self.size_threshold:
                break
            else:
                for key,value in d.items():
                    if value==max_benefit:
                        clique.append(key)
                        nodes.remove(key)
        return clique

if __name__ == '__main__':
    extendClique = ExtendFeatureClique()
    f=open('extended_feature_cliques.csv','w')
    f.write('UserId,Predicted\n')
    for filename in os.listdir('./top_cliques/'):
        index=filename.split('.clique')[0]
        f.write(index+',')
        filepath = './top_cliques/' + filename
        flag=True
        for line in file(filepath):
            clique=line.split(' ')
            res=extendClique.extend(clique,index)
            if flag:
                flag=False
                f.write(' '.join(res))
            else:
                f.write(';')
                f.write(' '.join(res))
        f.write('\n')
    f.close()
