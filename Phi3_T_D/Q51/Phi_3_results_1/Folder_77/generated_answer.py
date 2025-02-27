def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        s1, s2 = (s1.lower(), s2.lower())
        return len(s1) == len(s2) and sorted(s1) == sorted(s2) and (3 <= len(s1) <= len(s2))
    anagram_count = 0
    checked_pairs = set()
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if (i, j) not in checked_pairs and is_anagram(strings[i], strings[j]):
                anagram_count += 1
                checked_pairs.add((i, j))
                checked_pairs.add((j, i))
    return anagram_count <= 17