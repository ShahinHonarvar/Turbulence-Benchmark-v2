def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1) == sorted(s2)
    anagram_pairs = set()
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            str1, str2 = (strings[i].lower(), strings[j].lower())
            if len(str1) >= 3 and len(str2) >= 3 and is_anagram(str1, str2):
                anagram_pairs.add(tuple(sorted([str1, str2])))
    return len(anagram_pairs) <= 50