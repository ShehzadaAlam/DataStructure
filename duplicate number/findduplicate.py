def contains_duplicates(array_list):
    hash_set = set()
    for elem in array_list:
        if elem in hash_set:
            return True
        hash_set.add(elem)
    return False
