from itertools import combinations

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    for first, second in combinations(strings, 2):
        if len(first) >= 3 and len(second) >= 3 and (normalize(first) == normalize(second)):
            anagram_count += 1
            if anagram_count > 89:
                return False
    return True