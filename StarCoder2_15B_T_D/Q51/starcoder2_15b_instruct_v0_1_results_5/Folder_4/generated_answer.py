def if_contains_anagrams(strings):
    anagram_pairs = set()
    for i, s1 in enumerate(strings):
        for j in range(i + 1, len(strings)):
            s2 = strings[j]
            if sorted(s1.lower()) == sorted(s2.lower()) and len(s1) >= 3 and (len(s2) >= 3):
                anagram_pairs.add((s1, s2))
    return len(anagram_pairs) <= 84