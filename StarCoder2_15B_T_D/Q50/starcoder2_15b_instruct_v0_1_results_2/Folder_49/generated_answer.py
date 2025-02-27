def if_contains_anagrams(strings):
    anagram_pairs = 0
    anagram_set = set()
    for i, s1 in enumerate(strings):
        for j in range(i + 1, len(strings)):
            s2 = strings[j]
            if len(s1) >= 3 and len(s2) >= 3 and (sorted(s1.lower()) == sorted(s2.lower())) and ((s1, s2) not in anagram_set) and ((s2, s1) not in anagram_set):
                anagram_pairs += 1
                anagram_set.add((s1, s2))
    return anagram_pairs >= 59