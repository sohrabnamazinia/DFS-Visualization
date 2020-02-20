import pygame
import math
import time
t = input()
t = t.split()
n = int(t[0])
m = int(t[1])
edgelist = []
graphlist = []

for i in range(m):
    edge = input()
    edge = edge.split()
    edgelist.append([int(edge[0]) , int(edge[1])])

for i in range(n):
    graphlist.append([])

def make_graph(edgelist , graph):
    for i in edgelist :
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    return graph

def sort_graph(graph):
    answerlist = []
    for i in graph:
        i.sort()
        answerlist.append(i)
    return answerlist

graflist = sort_graph(make_graph(edgelist , graphlist))

class node:
    def __init__(self,name,neibor,coordinate,color):
        self.name = name
        self.neibor = neibor
        self.coordinate = coordinate
        self.color = color
    
    def get_name(self):
        return self.name

    def get_neibor(self):
        return self.neibor

    def get_coordinate(self):
        return self.coordinate

    def get_color(self):
        return self.color

    def change_name(self,newname):
        self.name = newname

    def change_neibor(self,newneibor):
        self.neibor = newneibor

    def change_coordinate(self,newcoordinate):
        self.coordinate = newcoordinate

    def change_color(self,newcolor):
        self.color = newcolor

class EDGE:
    def __init__(self,edge,color):
        self.edge = edge
        self.color =color
    
    def get_edge(self):
        return self.edge
    
    def get_color(self):
        return self.color

    def change_color(self,new_color):
        self.color = new_color

class graph:
    def __init__(self,nodelist,edgelist):
        self.nodelist = nodelist
        self.edgelist = edgelist

    def get_nodelist(self):
        return self.nodelist
    
    def drawing(self,win):
        font = pygame.font.SysFont("comicsansms", 20)
        for i in (range(len(self.edgelist))):
            Edge = self.edgelist[i].get_edge()
            pygame.draw.line(win , self.edgelist[i].get_color() , self.nodelist[Edge[0]].get_coordinate() , self.nodelist[Edge[1]].get_coordinate(), 2)
        for i in range(len(self.nodelist)):
            text = font.render(str(self.nodelist[i].get_name()), True, (0, 128, 0))
            pygame.draw.circle(win,self.nodelist[i].get_color(),self.nodelist[i].get_coordinate(),20)
            win.blit(text,self.nodelist[i].get_coordinate())
        pygame.display.update()

    def dfs(self):
        visited = []
        dfs_route = []
        answer_DFS = []

        def make_route(v):
            route = []
            for i in range(len(v) - 1):
                route.append([v[i] , v[i+1]])
            return route
        def in_list(list1,list2):
            answer = True
            for i in list1 :
                if not(i in list2):
                    answer = False
            return answer

        def DFS(nodelist,start_node):
            if not(start_node in visited):
                visited.append(start_node)
                dfs_route.append(start_node)
            counter = 0
            help_visited = visited.copy()
            answer_DFS.append([help_visited , make_route(dfs_route)])
            for i in self.nodelist[start_node].get_neibor():
                if not(i in visited):
                    counter += 1
                    DFS(nodelist , i)
            if counter == 0 :
                if len(dfs_route) > 1:
                    if in_list(nodelist[dfs_route[-1]].get_neibor() , visited):
                        start_node = dfs_route.pop()
                    else:
                        start_node = dfs_route[-1]
                    DFS(nodelist , start_node)
            return answer_DFS
        answer = DFS(self.nodelist , 0)
        return answer
                

# make list of node
nodelist = []
point = [250,250]
alfa = 0
for i in range(len(graphlist)):
    newpoint = (point[0] +  int((20 * len(graflist)) * math.cos(alfa)) , point[1] + int((20 * len(graflist)) * math.sin(alfa)))
    nodelist.append(node(i,graphlist[i],newpoint,(255,0,0)))
    alfa += (2 * math.pi) / len(graflist)

#make list of edge objects
for i in range(len(edgelist)):
    edgelist[i] = EDGE(edgelist[i] , ((255,255,0)))

g = graph(nodelist , edgelist)
answerlist = g.dfs()       


def main(nodelist , edgelist):
    pygame.init()
    win = pygame.display.set_mode((500 , 500))
    pygame.display.set_caption('dfs_project')

    win.fill((255, 255, 255))
    g.drawing(win)
    pygame.display.update()
    for i in answerlist:
        for j in i[0]:
            nodelist[j].change_color((100,100,200))
        for j in i[1]:
            for k in edgelist:
                if k.get_edge() == j:
                    k.change_color((255,0,0))
                g.drawing(win)
                pygame.display.update()
        for j in range(len(edgelist)):
            if not(edgelist[j].get_edge() in i[1]):
                edgelist[j].change_color((255,255,0))
                g.drawing(win)
                pygame.display.update()
        win.fill((255,255,255))
        g.drawing(win)
        pygame.display.update()
        time.sleep(1)
    pygame.display.quit()

if __name__ == '__main__':
    main(nodelist,edgelist)
