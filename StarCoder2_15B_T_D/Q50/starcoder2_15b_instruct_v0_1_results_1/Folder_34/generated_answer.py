def if_contains_anagrams(list_of_strings):
    anagram_pairs = 0
    for i in range(len(list_of_strings)):
        for j in range(i + 1, len(list_of_strings)):
            word1 = list_of_strings[i].lower()
            word2 = list_of_strings[j].lower()
            if len(word1) >= 3 and len(word2) >= 3 and (sorted(word1) == sorted(word2)):
                anagram_pairs += 1
    return anagram_pairs >= 25