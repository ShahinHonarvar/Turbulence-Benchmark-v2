def if_contains_anagrams(strings):
    anagram_pairs = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                anagram_pairs += 1
                if anagram_pairs > 70:
                    return False
    return True

def is_anagram(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    if len(s1) >= 3 and len(s2) >= 3:
        s1 = ''.join((c for c in s1 if c.isalpha()))
        s2 = ''.join((c for c in s2 if c.isalpha()))
        return sorted(s1) == sorted(s2)
    else:
        return False