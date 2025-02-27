def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        s1, s2 = (s1.lower(), s2.lower())
        return sorted(s1) == sorted(s2)
    filtered_strings = [s for s in strings if len(s) >= 3]
    anagram_pairs = 0
    for i in range(len(filtered_strings) - 1):
        for j in range(i + 1, len(filtered_strings)):
            if is_anagram(filtered_strings[i], filtered_strings[j]):
                anagram_pairs += 1
    return anagram_pairs <= 59