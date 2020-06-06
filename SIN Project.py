import networkx as nx 
import matplotlib.pyplot as plt 
from operator import itemgetter

print("Enter the random graph parameters") 
l = input().split(" ") 
print("") 
n = int(l[0]) 
p = float(l[1]) 
G = nx.fast_gnp_random_graph(n, p, seed=None, directed=False)

def bought_together(graph, user):     
    return set(graph.neighbors(user)) 

def nieghbour(graph, user):     
    x=[]     
    for each in graph.neighbors(user):         
        for item in graph.neighbors(each):             
            x.append(item)     
    return set(x)

def common_neighbour(graph, user1, user2):     
    x1 = bought_together(graph, user1)     
    x2 = bought_together(graph, user2)     
    return set(x1&x2)

def number_of_common_neighbour_map(graph, user): 
    new_dict = dict()     
    for each in graph.nodes():         
        if(each!=user):             
            if(each not in graph.neighbors(user)):                 
                new_dict[each] = len(common_neighbour(graph,each,user))     
    return new_dict

def number_map_to_sorted_list(map):     
    map = sorted(map.items(), key = itemgetter(1), reverse=True)     
    return map

def recommend_by_number_of_common_friends(graph, user):        
    diction = dict()     
    diction = number_of_common_neighbour_map(graph,user)     
    diction = number_map_to_sorted_list(diction)     
    recommendations = []     
    for i in range(0,10): 
        recommendations.append(diction[i])     
    return recommendations

def calc_score(graph, user, each):     
    score = 0     
    common = common_neighbour(graph, user, each)     
    for item in common:         
        score = score + 1/(len(bought_together(graph, item)))     
    return score

def influence_map(graph, user):     
    influence_scores = dict()     
    for each in graph.nodes():         
        if(each != user):             
            score = calc_score(graph, user, each)             
            influence_scores[each] = score     
    return influence_scores      

def recommend_by_influence(graph, user):     
    recommendations = [] 
    d=influence_map(graph,user)     
    d = sorted(d.items(), key = itemgetter(1), reverse=True)     
    for i in range(0,10):         
        recommendations.append(d[i])     
    return recommendations

def return_pure_list(recommendations):     
    pure_list = []     
    for each in recommendations:         
        pure_list.append(each[0])     
    return pure_list

def most_common(lst):     
    return max(set(lst), key=lst.count)

def show(graph, user):     
    plt.clf()
    nx.draw_networkx_nodes(graph, pos=nx.random_layout(graph), nodelist=return_pure_list(recommend_by_influence(graph,user)), node_color='r',node_size=500, alpha=0.8)     
    plt.gcf()     
    plt.savefig('plot.jpg')
    plt.title("GRAPH")     
    print("Recommendation by influence: ")     
    print(recommend_by_influence(graph, user))     
    print("Recommendation by Frequently bought together: ")     
    print(recommend_by_number_of_common_friends(graph, user))
    
def draw(G):     
    nx.draw(G)     
    plt.gcf()     
    plt.savefig("graph.jpg")
    
print("Enter the node:") 
node = int(input()) 
draw(G) 
show(G,node)
