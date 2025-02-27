from itertools import combinations

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    count = 0
    for pair in combinations(strings, 2):
        if len(pair[0]) >= 3 and len(pair[1]) >= 3:
            if normalize(pair[0]) == normalize(pair[1]):
                count += 1
    return count >= 81