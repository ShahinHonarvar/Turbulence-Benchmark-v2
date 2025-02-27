import collections

def if_contains_anagrams(strings):
    anagram_groups = collections.defaultdict(list)
    for string in strings:
        normalized_string = ''.join((c for c in string.lower() if c.isalpha()))
        if len(normalized_string) >= 3:
            anagram_groups[tuple(sorted(normalized_string))].append(string)
    return len(anagram_groups) <= 116