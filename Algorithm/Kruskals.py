class Edge:

    def __init__(self,src,dest,weight) -> None:
        self.source=src
        self.destination=dest
        self.weight=weight
        pass

    def __str__(self) -> str:
        return "{} - {} = {}".format(self.source,self.destination,self.weight)

class kruskals:

    def __init__(self,vertices,edges,nodes) -> None:
        self.vertices_count = vertices
        self.edges_count = edges
        self.edges = nodes
        pass

    class Subset:
        def __init__(self,parent) -> None:
            self.parent = parent
            pass

    def algorithmProcess(self):
        self.subset =[]
        self.resultSet=[]
        for i in range(self.vertices_count):
            self.subset.append(self.Subset(i))
        self.edges = sorted(self.edges,key=lambda x:x.weight)
        e,i=0,0
        while(e<self.vertices_count and i<self.edges_count):
            edge = self.edges[i]
            print(edge)
            x=self.getSubsetParent(edge.source)
            y=self.getSubsetParent(edge.destination)
            print("sorce and destination is {},{} and {} {}".format(x,y,edge.source,edge.destination))
            if x!=y:
                self.changeParent(x,y)
                self.resultSet.append(edge)
                e+=1
            i+=1
        return self.resultSet

    def getSubsetParent(self,vertice):
        if(self.subset[vertice].parent != vertice):
            return self.getSubsetParent(self.subset[vertice].parent)
        return self.subset[vertice].parent

    def changeParent(self,x,y):
        self.subset[y]=self.Subset(x)

if __name__=="__main__":
    vertices = int(input())
    edges_count = int(input())
    edges=[]
    for i in range(edges_count):
        userInput=input().split()
        # edges.append(Edge(int(input()),int(input()),int(input())))
        edges.append(Edge(int(userInput[0]),int(userInput[1]),int(userInput[2])))

    kruskalAlgorithm = kruskals(vertices,edges_count,edges)
    result = kruskalAlgorithm.algorithmProcess()
    for i in result:
        print(i)


# 4
# 6
# 0 1 5
# 0 2 3
# 3 0 6
# 1 3 7
# 2 1 4
# 2 3 5


# 4
# 6
# 1 2 5
# 1 3 3
# 4 1 6
# 2 4 7
# 3 2 4
# 3 4 5


# 9
# 14
# 0 1 4
# 0 7 8
# 7 1 11
# 1 2 8
# 7 6 1
# 7 8 7
# 6 8 6
# 8 2 2
# 6 5 2
# 2 5 4
# 2 3 7
# 5 4 10
# 5 3 14
# 3 4 9
    