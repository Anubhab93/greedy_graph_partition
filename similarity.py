from collections import Counter

def check_two_clusters_similar(a, b):

    """
    :param a: one cluster - a list
    :param b: another cluster - another list
    :return: if the lists are identical regardless of the order, returns True, else returns false
    """
    if len(a) == 0:
        return False
    elif len(b) == 0:
        return False
    else:
        return Counter(a) == Counter(b)

def check_all_clusters_similar(cla, clb):

    """
    :param cla: a 2D matrix, where each rows corresponds to one cluster
    :param clb: another 2D matrix, where each rows corresponds to one cluster
    :return: True if all clusters are same, otherwise false
    """

    if len(cla) == len(clb):
        no_rows = len(cla)
        no_similar = 0
        count = 0
        while count < no_rows:
            j = 0
            while j < no_rows:
                dcsn = check_two_clusters_similar(cla[count], clb[j])
                if dcsn:
                    no_similar += 1
                    break
                else:
                    j += 1
            count += 1
        if no_similar == no_rows:
            return True
        else:
            return False
    else:
        return False


if __name__ == "__main__":

    x = [[9, 3, 4], [5, 6, 7]]
    y = [[6, 5, 7], [3, 4, 9]]
    print(check_all_clusters_similar(x,y))