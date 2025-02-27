def if_contains_anagrams(strings):
    pairs_of_anagrams = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if sorted(strings[i].lower()) == sorted(strings[j].lower()) and len(strings[i]) >= 3:
                pairs_of_anagrams += 1
    return pairs_of_anagrams >= 123