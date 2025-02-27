def if_contains_anagrams(string_list):
    anagram_pairs = 0
    for string1 in string_list:
        for string2 in string_list:
            if len(string1) >= 3 and len(string2) >= 3 and (sorted(string1.lower()) == sorted(string2.lower())):
                anagram_pairs += 1
    return anagram_pairs >= 194