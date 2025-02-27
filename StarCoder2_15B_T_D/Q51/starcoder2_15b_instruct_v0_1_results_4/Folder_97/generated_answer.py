def if_contains_anagrams(list_of_strings):
    anagram_pairs = 0
    for i in range(len(list_of_strings)):
        for j in range(i + 1, len(list_of_strings)):
            if sorted(list_of_strings[i].lower()) == sorted(list_of_strings[j].lower()) and len(list_of_strings[i]) >= 3 and (len(list_of_strings[j]) >= 3):
                anagram_pairs += 1
                if anagram_pairs > 18:
                    return False
    return anagram_pairs <= 18