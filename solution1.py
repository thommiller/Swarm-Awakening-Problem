import sys,math,itertools,matplotlib
from matplotlib import pyplot as plt
from shapely.geometry.polygon import LinearRing, LineString
import numpy as np
import networkx as nx

# method for plotting the robots and obstacles using matplotlib
def plot_graph(robots,obstacles):
    # split the graph into subplots for plotting robots & obstacles on same graph
    fig, ax = plt.subplots()
    graph = nx.Graph()
    # nodes are labelled 0,1,...,n where n = number of robots
    nodes=range(len(robots))
    # edges map each node to every other node
    edges=list(itertools.product(nodes,nodes))
    # add all edges and nodes to graph
    graph.add_nodes_from(nodes,pos=robots)
    graph.add_edges_from(edges)
    nx.draw(graph,pos=robots)

    #plot obstacles
    for obstacle in obstacles:
        ring = LinearRing(obstacle)
        #calculate their intersections with any edges
        print(ring.intersection(LineString(edges)))
        x, y = ring.xy
        ax.plot(x, y)
    plt.show()


# foreach robot, wake up the next robot, let those two robots wake up the next two robots etc...
def in_order(robots, obstacles):
    plot_graph(robots,obstacles)


if __name__ == '__main__':
    problemlist = open('robots.mat','r')
    # robots read in as::
    # <list of robots>#<list of vertices of obstacle>;<next list of obstacle vertices>
    for row in problemlist:
        robots = [tuple(list(map(int,x.split(",")))) for x in (row[4:-1].split("#")[0][:-1].split("),("))]
        try:
            obstacles = [[tuple(list(map(int,coord.split(",")))) for coord in obstacle.split("),(")] for obstacle in row.split("#")[1][1:-2].split(");(")]
        except:
            obstacles = []
        print('robots: ', robots)
        print('obstacles: ', obstacles)
        print('')

        in_order(robots,obstacles)
