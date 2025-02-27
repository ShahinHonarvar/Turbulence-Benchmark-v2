from collections import Counter

def if_contains_anagrams(strings):
    strings = [s.lower() for s in strings]
    anagram_dict = {}
    for s in strings:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            if sorted_s in anagram_dict:
                anagram_dict[sorted_s].append(s)
            else:
                anagram_dict[sorted_s] = [s]
    anagram_counts = Counter([len(v) for v in anagram_dict.values()])
    pairs = sum([n * (n - 1) // 2 for n in anagram_counts if n > 1])
    return pairs >= 94