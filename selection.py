import networkx as nx

def select_first_node(g):

    """
    :param g: the graph
    :return: the first node of the node sequence based on which the graph will be partitioned. We select the first node
    as the node which has the lowest degree
    """
    all_degrees = []
    node_list = list(range(0, len(g)))
    for node in node_list:
        all_degrees.append(g.degree[node])
    return all_degrees.index(min(all_degrees))

def generate_node_selection_sequence(g):

    """
    :param g: the graph
    :return: generates a sequence how the nodes will be selected in sequence for the greedy partitioning algorithm
    """

    next_nodes_to_visit = []
    node_sequence = []
    next_nodes_to_visit.append(select_first_node(g))
    while len(next_nodes_to_visit) >= 1:
        nnode = next_nodes_to_visit[0]
        if nnode not in node_sequence:
            next_nodes_to_visit.remove(nnode)
            node_sequence.append(nnode)
            all_neighbors = [n for n in g.neighbors(nnode)]
            for x in all_neighbors:
                if x not in node_sequence:
                    next_nodes_to_visit.append(x)
        else:
            next_nodes_to_visit.remove(nnode)

    return node_sequence

if __name__ == "__main__":

    nous_list = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90]
    p_list = [0.2, 0.5, 0.8]
    for nous in nous_list:
        for p in p_list:
            g = nx.read_yaml('graphs/node_{}_p_{}.yaml'.format(str(nous), str(p).replace(".", "")))
            nodeseq = len(generate_node_selection_sequence(g))
            if nodeseq == len(g):
                print("Passed\n")
            else:
                print("FAIL!\n")
