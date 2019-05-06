import networkx as nx
from itertools import combinations

def include_node_into_cluster(g, new_node, other_nodes, max_hop):

    """
    :param g: graph
    :param new_node: selected node
    :param other_nodes: other nodes which are already in the cluster
    :return: if new node is at most k hops away from all other nodes, returns True, else return False
    """

    check_val = 0
    for otnode in other_nodes:
        if nx.shortest_path_length(g, source=new_node, target=otnode) <= max_hop:
            check_val += 1
    if check_val == len(other_nodes):
        return True
    else:
        return False

def generate_graph_from_node_list(g, node_list):

    new_graph = nx.Graph()
    new_graph.add_nodes_from(node_list)
    c = list(combinations(node_list, 2))
    for (u,v) in c:
        if g.has_edge(u,v):
            new_graph.add_edge(u,v)
    return new_graph

if __name__ == "__main__":

    g = nx.Graph()
    node_list = [1, 2, 3, 4, 5, 6]
    print(generate_graph_from_node_list(g, node_list))

