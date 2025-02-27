def if_contains_anagrams(strings):
    anagram_pairs = 0
    for i, string1 in enumerate(strings):
        for j in range(i + 1, len(strings)):
            string2 = strings[j]
            if sorted(string1.lower()) == sorted(string2.lower()) and len(string1) >= 3 and (len(string2) >= 3):
                anagram_pairs += 1
                if anagram_pairs > 68:
                    return False
    return anagram_pairs <= 68