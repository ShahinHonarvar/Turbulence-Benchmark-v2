from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_count = 0
    seen_anagrams = defaultdict(int)
    for s in lst:
        s = s.lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            if seen_anagrams[sorted_s] > 0:
                anagram_count += seen_anagrams[sorted_s]
                if anagram_count > 72:
                    return False
            seen_anagrams[sorted_s] += 1
    return True