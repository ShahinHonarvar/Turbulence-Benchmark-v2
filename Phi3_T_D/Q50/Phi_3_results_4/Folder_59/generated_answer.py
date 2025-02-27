import itertools

def if_contains_anagrams(strings):
    anagram_pairs = 0
    strings = [string.lower() for string in strings]
    for str1, str2 in itertools.combinations(strings, 2):
        if len(str1) >= 3 and len(str2) >= 3 and (sorted(str1) == sorted(str2)):
            anagram_pairs += 1
            if anagram_pairs >= 10:
                return True
    return False