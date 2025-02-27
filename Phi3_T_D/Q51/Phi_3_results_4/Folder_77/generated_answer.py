from itertools import combinations

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        if len(s1) < 3 or len(s2) < 3:
            return False
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_count = 0
    for pair in combinations(strings, 2):
        if is_anagram(pair[0], pair[1]):
            anagram_count += 1
            if anagram_count > 17:
                return False
    return True