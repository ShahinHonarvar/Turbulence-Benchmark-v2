from collections import defaultdict

def if_contains_anagrams(strings):

    def count_chars(s):
        return sorted(s.lower())
    counts = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            key = tuple(count_chars(string))
            counts[key].append(string)
    anagram_pairs = sum((len(v) >= 2 for v in counts.values()))
    return anagram_pairs >= 21