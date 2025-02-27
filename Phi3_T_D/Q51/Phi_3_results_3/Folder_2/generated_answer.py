from itertools import combinations

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    count = 0
    for string_pair in combinations(strings, 2):
        if len(string_pair[0]) >= 3 and len(string_pair[1]) >= 3 and is_anagram(*string_pair):
            count += 1
            if count > 81:
                return False
    return True