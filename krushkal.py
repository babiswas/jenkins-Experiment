class Sub:
   def __init__(self,parent,rank):
       self.parent=parent
       self.rank=rank

class Graph:
   def __init__(self,vertex):
      self.vertex=vertex
      self.graph=list()

   def add_edges(self,u,v,w):
      self.graph.append((u,v,w))


   def find(self,u,parent):
       while parent[u].parent!=-1:
           u=parent[u].parent
       return u

   def union(self,u,v,parent):
       index1=self.find(u,parent)
       index2=self.find(v,parent)
       if index1!=index2:
          if parent[u].rank>parent[v].rank:
             parent[v].parent=u
             parent[u].rank=parent[u].rank+1
          elif parent[v].rank>parent[u].rank:
             parent[u].parent=v
             parent[v].rank=parent[v].rank+1
          else:
             parent[u].parent=v
             parent[v].rank=parent[v].rank+1

   def krushkal_algo(self):
       edge=list()
       parent=[Sub(-1,0) for i in range(self.vertex)]
       def getitem(obj):
           return obj[2]
       self.graph=sorted(self.graph,key=getitem)
       for u,v,w in self.graph:
          index1=self.find(u,parent)
          index2=self.find(v,parent)
          if index1!=index2:
             self.union(index1,index2,parent)
             edge.append((u,v,w))
       print(edge)


if __name__=="__main__":
   graph=Graph(9)
   graph.add_edges(0,1,4)
   graph.add_edges(0,7,8)
   graph.add_edges(1,7,11)
   graph.add_edges(7,8,7)
   graph.add_edges(7,6,1)
   graph.add_edges(8,6,6)
   graph.add_edges(1,2,8)
   graph.add_edges(2,8,2)
   graph.add_edges(6,5,2)
   graph.add_edges(2,5,4)
   graph.add_edges(2,3,7)
   graph.add_edges(3,5,14)
   graph.add_edges(5,4,10)
   graph.add_edges(3,4,9)
   graph.krushkal_algo()
   print("hello")
   print("bello")
   print("mello")
   print("chilloo")
   

           
          