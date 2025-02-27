def is_anagram(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    if len(s1) != len(s2):
        return False
    s1_sorted = sorted(s1)
    s2_sorted = sorted(s2)
    for c1, c2 in zip(s1_sorted, s2_sorted):
        if c1 != c2:
            return False
    return True

def if_contains_anagrams(strings):
    anagrams = []
    for s in strings:
        if is_anagram(s, 'abcdefghijklmnopqrstuvwxyz'):
            anagrams.append(s)
    if len(anagrams) > 85:
        return False
    return True