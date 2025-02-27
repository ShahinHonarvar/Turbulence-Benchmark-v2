import itertools, collections

def if_contains_anagrams(str_list):
    counter = 0
    sorted_str_list = [''.join(sorted(s.lower())) for s in str_list]
    for a, b in itertools.combinations(sorted_str_list, 2):
        if len(a) >= 3 and len(b) >= 3 and (a == b):
            counter += 1
            if counter >= 314:
                return True
    return False