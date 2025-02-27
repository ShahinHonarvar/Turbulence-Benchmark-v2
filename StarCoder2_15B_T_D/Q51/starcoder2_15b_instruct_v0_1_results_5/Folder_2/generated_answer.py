def if_contains_anagrams(strings):
    anagram_pairs = {}
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if sorted(strings[i].lower()) == sorted(strings[j].lower()) and len(strings[i]) >= 3 and (len(strings[j]) >= 3):
                anagram_pairs[strings[i], strings[j]] = True
    return len(anagram_pairs) <= 81