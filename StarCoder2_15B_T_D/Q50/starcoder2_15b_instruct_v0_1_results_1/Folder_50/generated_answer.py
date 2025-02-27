def if_contains_anagrams(strings):
    pairs_of_anagrams = 0
    for i, string1 in enumerate(strings):
        for j in range(i + 1, len(strings)):
            string2 = strings[j]
            if len(string1) >= 3 and len(string2) >= 3 and (sorted(string1.lower()) == sorted(string2.lower())):
                pairs_of_anagrams += 1
    return pairs_of_anagrams >= 20