def if_contains_anagrams(strings):

    def are_anagrams(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_count = 0
    for i, s1 in enumerate(strings):
        for s2 in strings[i + 1:]:
            if are_anagrams(s1, s2):
                anagram_count += 1
    return anagram_count >= 72