from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = defaultdict(int)
    for s in strings:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            sorted_s = ''.join(sorted(s_lower))
            anagram_count[sorted_s] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_count.values() if count > 1))
    return anagram_pairs >= 411