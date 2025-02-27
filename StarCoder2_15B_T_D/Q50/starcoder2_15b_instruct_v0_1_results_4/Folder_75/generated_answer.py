def if_contains_anagrams(strings):
    anagram_pairs = 0
    for i, string1 in enumerate(strings):
        for j, string2 in enumerate(strings):
            if i != j and len(string1) >= 3 and (len(string2) >= 3) and (sorted(string1.lower()) == sorted(string2.lower())):
                anagram_pairs += 1
    return anagram_pairs >= 70