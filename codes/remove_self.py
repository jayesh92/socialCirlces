import os

# Sagar op's *.bestk
os.system('rm ./top_cliques/*.clique')

# read all best k
# remove first node
# remove all *bestk
# generate .cliques without self(first) node
for filename in os.listdir('./top_cliques'):
    index= filename.split('.cliques.bestk')[0]
    f=open('./top_cliques/' + str(index) + '.clique','w')
    for line in file('./top_cliques/'+filename):
        x=line.split(' ')[1:]
        f.write(' '.join(x))
    f.close()
    os.system('rm ./top_cliques/' + filename)

f=open('./top_cliques.csv','w')
f.write('UserId,Predicted\n')
for filename in os.listdir('./top_cliques'):
    index= filename.split('.clique')[0]
    f.write(index+',')
    flag=True
    for line in file('./top_cliques/'+filename):
        x=line.split(' ')
        x[-1]=x[-1].strip('\n')
        if flag:
            f.write(' '.join(x))
            flag=False
        else:
            f.write(';')
            f.write(' '.join(x))
    f.write('\n')
f.close()
