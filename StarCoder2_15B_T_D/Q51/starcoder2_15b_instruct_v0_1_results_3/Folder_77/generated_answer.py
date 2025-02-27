def if_contains_anagrams(strings):
    anagram_pairs = 0
    for i, s1 in enumerate(strings):
        for j in range(i + 1, len(strings)):
            s2 = strings[j]
            if sorted(s1.lower()) == sorted(s2.lower()) and len(s1) >= 3 and (len(s2) >= 3):
                anagram_pairs += 1
                if anagram_pairs > 17:
                    return False
    return anagram_pairs <= 17