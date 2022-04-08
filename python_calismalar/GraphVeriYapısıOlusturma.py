#Graph Veri Yapısı Oluşturma
class graph:
    def __init__(self,weighted,directed) :
        self.weighted = weighted
        self.directeed = directed
        self.graphDict = {}
        
    dict = {
        
        "A" : [("B",7),("C",8)],
        "B" : [("A",7)],
        "C" : [("A",8)],
    }
    
    def addNode(self,nodeName): 
        if nodeName not in self.graphDict:
            self.graphDict[nodeName] = []
    
    def addEdge(self,node1,node2,weight):
        if node1 not in self.graphDict:
            return   
        if node2 not in self.graphDict:
            return  
        if self.directeed == False:
            self.graphDict[node1].append((node2,weight))
            self.graphDict[node2].append((node1,weight))
        else:
            self.graphDict[node1].append((node2,weight))
                
            
gr = graph(False,False)
gr.addNode("A")
gr.addNode("B")
gr.addNode("C")
gr.addNode("D")
gr.addNode("E")

gr.addEdge("A","B",5)
gr.addEdge("A","C",3)
gr.addEdge("A","D",8)

gr.addEdge("B","D",7)
gr.addEdge("E","D",2)
gr.addEdge("C","D",4)
gr.addEdge("D","D",1)

print(gr.graphDict)

for key, value in gr.graphDict.items():
    print(key + "->" , end=(''))
    for i in value:
        print(str(i[0]) + " : " + str(i[1]) , end=(''))
    print(" ")    
    
