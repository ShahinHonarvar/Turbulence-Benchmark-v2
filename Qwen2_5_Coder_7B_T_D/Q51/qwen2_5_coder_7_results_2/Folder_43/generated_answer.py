from collections import Counter

def if_contains_anagrams(lst):
    anagram_pairs = 0
    seen = set()
    for s in lst:
        s = s.lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            if sorted_s in seen:
                anagram_pairs += 1
                if anagram_pairs > 3:
                    return False
                seen = {sorted_s}
            else:
                seen.add(sorted_s)
    return anagram_pairs <= 3