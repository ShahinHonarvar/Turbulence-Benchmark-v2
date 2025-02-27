from itertools import combinations

def if_contains_anagrams(strings_list):

    def char_count(s):
        return ''.join(sorted(s.lower()))
    count_anagrams = 0
    for a, b in combinations(strings_list, 2):
        if len(a) >= 3 and len(b) >= 3 and (char_count(a) == char_count(b)):
            count_anagrams += 1
            if count_anagrams > 113:
                return False
    return True