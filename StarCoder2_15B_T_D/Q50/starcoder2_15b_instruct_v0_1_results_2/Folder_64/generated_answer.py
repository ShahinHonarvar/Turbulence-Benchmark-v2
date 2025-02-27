def if_contains_anagrams(strings):
    anagram_pairs = 0
    for i, string_1 in enumerate(strings):
        for j in range(i + 1, len(strings)):
            string_2 = strings[j]
            if len(string_1) >= 3 and len(string_2) >= 3 and (sorted(string_1.lower()) == sorted(string_2.lower())):
                anagram_pairs += 1
                if anagram_pairs >= 5:
                    return True
    return False