from collections import Counter

def if_contains_anagrams(lst):
    anagram_count = 0
    seen_anagrams = {}
    for s in lst:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            sorted_s = ''.join(sorted(s_lower))
            if sorted_s in seen_anagrams:
                seen_anagrams[sorted_s] += 1
            else:
                seen_anagrams[sorted_s] = 1
    for count in seen_anagrams.values():
        if count > 1:
            anagram_count += count * (count - 1) // 2
    return anagram_count >= 18