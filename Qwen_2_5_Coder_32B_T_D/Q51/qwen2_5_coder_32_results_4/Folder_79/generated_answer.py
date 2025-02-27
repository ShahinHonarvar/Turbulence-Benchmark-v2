from itertools import combinations

def if_contains_anagrams(strings):

    def sorted_letters(s):
        return ''.join(sorted(s.lower()))
    valid_anagrams = 0
    for str1, str2 in combinations(strings, 2):
        if len(str1) >= 3 and len(str2) >= 3 and (sorted_letters(str1) == sorted_letters(str2)):
            valid_anagrams += 1
            if valid_anagrams > 173:
                return False
    return True