def if_contains_anagrams(strings):
    anagram_count = 0
    for i, string_1 in enumerate(strings):
        for j, string_2 in enumerate(strings):
            if i != j and len(string_1) >= 3 and (len(string_2) >= 3) and (sorted(string_1.lower()) == sorted(string_2.lower())):
                anagram_count += 1
    return anagram_count >= 15