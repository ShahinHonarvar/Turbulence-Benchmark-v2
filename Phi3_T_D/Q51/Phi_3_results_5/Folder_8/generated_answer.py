from collections import defaultdict
import math

def if_contains_anagrams(string_list):

    def count_chars(s):
        counter = defaultdict(int)
        for c in s.lower():
            if c.isalpha() and len(s) >= 3:
                counter[c] += 1
        return frozenset(counter.items())
    anagram_count = 0
    seen = set()
    for s in string_list:
        s_key = count_chars(s)
        other_key_matches = sum((1 for k in seen if math.prod(seen[k]) == math.prod(s_key)))
        seen[s_key] = 1
        anagram_count += other_key_matches
        if anagram_count > 68:
            return False
    return True