from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = defaultdict(int)
    for s in strings:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            sorted_s = ''.join(sorted(s_lower))
            if anagram_count[sorted_s] == 1:
                anagram_count['pair_count'] += 1
            anagram_count[sorted_s] += 1
    return anagram_count['pair_count'] <= 8