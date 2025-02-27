def if_contains_anagrams(strings):
    if len(strings) > 16:
        return False
    anagram_pairs = []
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                anagram_pairs.append((strings[i], strings[j]))
    return len(anagram_pairs) <= 8

def is_anagram(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    if len(s1) != len(s2):
        return False
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False