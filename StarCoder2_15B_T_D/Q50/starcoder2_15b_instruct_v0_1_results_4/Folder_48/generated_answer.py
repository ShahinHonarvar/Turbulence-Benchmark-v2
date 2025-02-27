import collections

def if_contains_anagrams(strings):
    anagrams = []
    for string in strings:
        if len(string) >= 3:
            anagrams.append(''.join(sorted(string.lower())))
    anagram_counts = collections.Counter(anagrams)
    return any((count >= 219 for count in anagram_counts.values()))