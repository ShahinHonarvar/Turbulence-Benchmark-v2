import itertools

def if_contains_anagrams(string_list):
    filtered_list = [''.join(sorted(s.lower())) for s in string_list if len(s) >= 3]
    anagrams_counter = 0
    for pair in itertools.combinations(filtered_list, 2):
        if pair[0] == pair[1]:
            anagrams_counter += 1
            if anagrams_counter > 79:
                return False
    return True