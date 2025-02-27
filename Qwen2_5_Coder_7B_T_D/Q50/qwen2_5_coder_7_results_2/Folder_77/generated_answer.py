from collections import defaultdict

def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return sorted(s1) == sorted(s2)
    count = 0
    anagrams = defaultdict(list)
    for s in lst:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            for other in anagrams[s_lower]:
                if is_anagram(s_lower, other):
                    count += 1
                    if count >= 209:
                        return True
            anagrams[s_lower].append(s_lower)
    return False