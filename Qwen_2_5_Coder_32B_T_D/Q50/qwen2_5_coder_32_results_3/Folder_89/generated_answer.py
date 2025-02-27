from collections import defaultdict

def if_contains_anagrams(strings):
    s_dict = defaultdict(int)
    for s in strings:
        s = s.lower()
        if len(s) >= 3:
            s_dict[''.join(sorted(s))] += 1
    anagram_pairs = 0
    for count in s_dict.values():
        anagram_pairs += count * (count - 1) // 2
    return anagram_pairs >= 36