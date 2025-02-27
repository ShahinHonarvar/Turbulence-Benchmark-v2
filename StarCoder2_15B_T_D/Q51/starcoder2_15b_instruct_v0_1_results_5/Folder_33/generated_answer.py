def if_contains_anagrams(strings):
    anagram_pairs = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            string1 = strings[i].lower()
            string2 = strings[j].lower()
            if sorted(string1) == sorted(string2) and len(string1) >= 3:
                anagram_pairs += 1
    return anagram_pairs <= 85