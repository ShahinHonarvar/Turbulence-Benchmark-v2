def if_contains_anagrams(list_of_strings):

    def are_anagrams(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    anagram_pairs = []
    for i in range(len(list_of_strings) - 1):
        for j in range(i + 1, len(list_of_strings)):
            if are_anagrams(list_of_strings[i], list_of_strings[j]):
                anagram_pairs.append((list_of_strings[i], list_of_strings[j]))
    return len(anagram_pairs) >= 59