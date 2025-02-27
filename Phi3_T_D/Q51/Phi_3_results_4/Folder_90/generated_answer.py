from itertools import combinations

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    counter = 0
    for string_pair in combinations(strings, 2):
        if len(string_pair[0]) >= 3 and len(string_pair[1]) >= 3 and (normalize(string_pair[0]) == normalize(string_pair[1])):
            counter += 1
            if counter > 147:
                return False
    return True