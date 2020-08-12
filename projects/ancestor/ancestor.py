
def earliest_ancestor(ancestors, starting_node):

    """
    Suppose we have some input data describing a graph of relationships between parents and 
    children over multiple generations. The data is formatted as a list of (parent, child) pairs, 
    where each individual is assigned a unique integer identifier.

    Write a function that, given the dataset and the ID of an individual in the dataset, returns 
    their earliest known ancestor – the one at the farthest distance from the input individual. 
    If there is more than one ancestor tied for "earliest", return the one with the lowest numeric ID. 
    If the input individual has no parents, the function should return -1.
    """
    
    # Can use a dict as cache, similar to hashtable
    cache = dict() #> dict to facilitate item assignment

    # Now let's make parents into an adjancency list
    for ancestor in ancestors:
        kid = ancestor[1]
        if kid not in cache:
            cache[kid] = set()
            cache[kid].add(ancestor[0])

        else:
            cache[kid].add(ancestor[0])
    
    kids = list(cache.keys())
    
    parents = set()
    for ancestor in ancestors:
        parents.add(ancestor[0])
    parents = list(parents) 

    if starting_node not in kids:
        return -1

    s = list()
    s.append(starting_node)

    seen = set()
    rents_ids = list()
    path = list()

    while len(s) > 0:
        # Sorting s forces the smallest value on any particular traversed level to go last
        s.sort()
        current = s.pop()

        if current not in seen:
            seen.add(current)
            path.append(current)
            
            if current in kids:
                rents_ids = list(cache[current])
                for ids in rents_ids:
                    s.append(ids)
    return path[-1]

if __name__ == "__main__":
    
    '''
       10
     /
    1   2   4  11
     \ /   / \ /
      3   5   8
       \ / \   \
        6   7   9
    '''

    test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    print(earliest_ancestor(test_ancestors, 1)) #> 10