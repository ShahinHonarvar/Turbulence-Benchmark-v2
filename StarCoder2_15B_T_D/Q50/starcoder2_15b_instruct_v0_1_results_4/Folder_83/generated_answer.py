def if_contains_anagrams(list_of_strings):
    anagram_pairs = 0
    for i, string1 in enumerate(list_of_strings):
        for j, string2 in enumerate(list_of_strings):
            if i != j and len(string1) >= 3 and (len(string2) >= 3) and (string1.lower() == string2.lower()[::-1]):
                anagram_pairs += 1
    return anagram_pairs >= 48