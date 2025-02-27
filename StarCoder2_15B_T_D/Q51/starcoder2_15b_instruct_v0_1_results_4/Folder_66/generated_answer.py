def if_contains_anagrams(strings):
    anagram_groups = {}
    for s in strings:
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagram_groups:
            anagram_groups[sorted_s].append(s)
        else:
            anagram_groups[sorted_s] = [s]
    return len(anagram_groups) <= 64

def is_anagram(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    s1 = ''.join(sorted(s1))
    s2 = ''.join(sorted(s2))
    return s1 == s2