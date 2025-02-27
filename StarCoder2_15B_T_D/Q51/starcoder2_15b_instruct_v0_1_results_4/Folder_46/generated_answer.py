import collections

def if_contains_anagrams(strings):
    anagram_groups = collections.defaultdict(list)
    for s in strings:
        s = s.lower()
        if len(s) >= 3:
            key = ''.join(sorted(s))
            anagram_groups[key].append(s)
    return len(anagram_groups) <= 61