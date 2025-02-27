def if_contains_anagrams(strings):
    anagram_pairs = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            str1 = sorted(strings[i].lower())
            str2 = sorted(strings[j].lower())
            if len(str1) >= 3 and len(str2) >= 3 and (str1 == str2):
                anagram_pairs += 1
                if anagram_pairs > 276:
                    return False
    return anagram_pairs <= 276