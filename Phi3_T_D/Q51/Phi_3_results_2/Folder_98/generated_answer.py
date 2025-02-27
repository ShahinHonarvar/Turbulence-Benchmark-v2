def sort_by_key(s):
    return ''.join(sorted(s)).lower()

def if_contains_anagrams(lst):
    sorted_lst = [sort_by_key(item) for item in lst]
    unique_sorted = set(sorted_lst)
    counter = 0
    for item in unique_sorted:
        occurrences = sorted_lst.count(item)
        if occurrences > 1 and len(item) >= 3:
            pairings = occurrences * (occurrences - 1) // 2
            counter += pairings
            if counter > 46:
                return False
    return True