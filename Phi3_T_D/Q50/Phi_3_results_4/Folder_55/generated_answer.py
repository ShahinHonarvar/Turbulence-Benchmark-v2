from collections import defaultdict

def if_contains_anagrams(strings):

    def count_chars(s):
        return ''.join(sorted(s.lower()))
    anagrams = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            key = count_chars(string)
            anagrams[key].append(string)
    pairs = sum((len(v) * (len(v) - 1) // 2 for v in anagrams.values()))
    return pairs >= 15