from collections import defaultdict

def if_contains_anagrams(strings):

    def are_anagrams(s1, s2):
        return len(s1) >= 3 and sorted(s1.lower()) == sorted(s2.lower())
    anagram_pairs = 0
    sorted_anagrams = defaultdict(list)
    for string in strings:
        sorted_str = tuple(sorted(string.lower()))
        sorted_anagrams[sorted_str].append(string)
    for group in sorted_anagrams.values():
        if len(group) > 1:
            anagram_pairs += sum((are_anagrams(string1, string2) for i, string1 in enumerate(group) for string2 in group[i + 1:]))
    return anagram_pairs >= 35