from collections import Counter

def if_contains_anagrams(lst):

    def sorted_string(s):
        return ''.join(sorted(s.lower()))
    anagram_pairs = 0
    seen = set()
    for s in lst:
        if len(s) >= 3:
            sorted_s = sorted_string(s)
            if sorted_s in seen:
                anagram_pairs += 1
            seen.add(sorted_s)
    return anagram_pairs >= 46