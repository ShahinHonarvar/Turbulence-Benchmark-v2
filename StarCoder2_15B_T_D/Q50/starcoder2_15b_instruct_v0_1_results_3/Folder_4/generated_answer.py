import itertools

def if_contains_anagrams(strings):
    anagram_groups = {}
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if sorted_string not in anagram_groups:
            anagram_groups[sorted_string] = [string]
        else:
            anagram_groups[sorted_string].append(string)
    anagram_pairs = sum((len(group) // 2 for group in anagram_groups.values()))
    return anagram_pairs >= 42