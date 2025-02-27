def if_contains_anagrams(strings):
    anagram_pairs = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                anagram_pairs += 1
                if anagram_pairs > 6:
                    return False
    return anagram_pairs <= 6

def is_anagram(s1, s2):
    s1 = sorted(s1.lower())
    s2 = sorted(s2.lower())
    return s1 == s2 and len(s1) >= 3