import itertools

def if_contains_anagrams(string_list):
    count_anagrams = 0
    for combo in itertools.combinations(string_list, 2):
        if len(combo[0]) >= 3 and len(combo[1]) >= 3:
            if sorted(combo[0].lower()) == sorted(combo[1].lower()):
                count_anagrams += 1
        if count_anagrams >= 7:
            return True
    return False