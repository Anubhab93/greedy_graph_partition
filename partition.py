import networkx as nx
import topology as tp
import matplotlib.pyplot as plt
import selection

def greedy_partition(g, max_hop, max_cluster_size, node_sequence):

    unvisited_nodes = list(g.nodes())
    cluster_id = 1
    cluster_dict = {}
    ndcount = 0
    while len(unvisited_nodes) > 0:
        stnode = node_sequence[ndcount]
        ndcount += 1
        if len(unvisited_nodes) == len(list(g.nodes())):
            cluster_dict[str(cluster_id)] = []
            cluster_dict[str(cluster_id)].append(stnode)
        else:
            ccount = 1
            cluster_sizes = []
            cluster_ids = []
            while ccount <= cluster_id:
                ccnodes = cluster_dict[str(ccount)]
                dcsn = tp.include_node_into_cluster(g, new_node=stnode, other_nodes=ccnodes, max_hop=max_hop)
                if dcsn:
                    cluster_sizes.append(len(ccnodes))
                    cluster_ids.append(ccount)
                ccount += 1
            if len(cluster_ids) <= 0:
                cluster_id += 1
                cluster_dict[str(cluster_id)] = []
                cluster_dict[str(cluster_id)].append(stnode)
            else:
                cluster_sizes.sort(reverse=True)
                k = 0
                not_added = True
                while k < len(cluster_sizes):
                    if cluster_sizes[k] <= max_cluster_size:
                        chosen_cluster = cluster_ids[k]
                        cluster_dict[str(chosen_cluster)].append(stnode)
                        not_added = False
                        break
                    k += 1
                if not_added:
                    chosen_cluster = cluster_ids[-1]
                    cluster_dict[str(chosen_cluster)].append(stnode)
        unvisited_nodes.remove(stnode)
    result = []
    for key,val in cluster_dict.items():
        result.append(val)
    return result

# def greedy_partition(g, max_hop, max_cluster_size):
#
#     all_result = []
#     is_converged = False
#     run_no = 1
#     while not is_converged:
#         print("Run Number: {}".format(run_no))
#         reslt = partition_single_run(g, max_hop=max_hop, max_cluster_size=max_cluster_size)
#         j = 0
#         while j < len(all_result):
#             dcsn = smt.check_all_clusters_similar(reslt, all_result[j])
#             if dcsn:
#                 print("final result: {}".format(reslt))
#                 is_converged = True
#                 break
#             else:
#                 all_result.append(reslt)
#         run_no += 1


if __name__ == "__main__":

    nous = 10
    p = 0.2
    g = nx.read_yaml('graphs/node_{}_p_{}.yaml'.format(str(nous), str(p).replace(".", "")))

    ### MAX_HOP 1
    ## [[2, 0], [1, 6], [3, 7], [5], [9], [4], [8]]
    ### MAX_HOP 2
    ## [[2, 0, 1, 3, 5], [6, 9], [7, 4, 8]]
    ### MAX_HOP 3
    ## [[2, 0, 1, 3, 5, 6, 9], [7, 4, 8]]

    node_seq = selection.generate_node_selection_sequence(g)
    all_lists = greedy_partition(g, max_hop=2, max_cluster_size=10, node_sequence=node_seq)
    print(all_lists)
    color_map = []
    color_list = ['b', 'g', 'r', 'c', 'm', 'y', 'grey', 'w', 'orange', 'tomato', 'coral', 'maroon']
    for node in g:
        j = 0
        while node not in all_lists[j]:
            j = j + 1
        color_map.append(color_list[j])
    print(color_map)
    nx.draw_kamada_kawai(g, node_color=color_map, with_labels=True)
    plt.show()