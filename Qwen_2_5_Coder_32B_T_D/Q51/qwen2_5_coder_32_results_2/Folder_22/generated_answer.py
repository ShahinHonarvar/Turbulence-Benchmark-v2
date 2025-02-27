from itertools import combinations

def if_contains_anagrams(lst):

    def sorted_characters(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    for a, b in combinations(lst, 2):
        if len(a) >= 3 and len(b) >= 3 and (sorted_characters(a) == sorted_characters(b)):
            anagram_count += 1
            if anagram_count > 14:
                return False
    return True