from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        return len(str1) >= 3 and sorted(str1.lower()) == sorted(str2.lower())
    anagrams_map = defaultdict(list)
    for s in strings:
        key = ''.join(sorted(s.lower()))
        anagrams_map[key].append(s)
    anagram_counts = sum((len(v) >= 2 for v in anagrams_map.values()))
    return anagram_counts >= 2