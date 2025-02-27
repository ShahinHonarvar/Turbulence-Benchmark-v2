def if_contains_anagrams(strings):
    anagram_pairs = set()
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            s1 = sorted(strings[i].lower())
            s2 = sorted(strings[j].lower())
            if s1 == s2 and len(strings[i]) >= 3:
                anagram_pairs.add(tuple(sorted([strings[i], strings[j]])))
    return len(anagram_pairs) >= 79