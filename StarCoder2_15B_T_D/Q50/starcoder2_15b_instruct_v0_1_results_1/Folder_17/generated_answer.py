def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    filtered_strings = [s for s in strings if len(s) >= 3]
    anagram_count = 0
    for i in range(len(filtered_strings) - 1):
        for j in range(i + 1, len(filtered_strings)):
            if is_anagram(filtered_strings[i], filtered_strings[j]):
                anagram_count += 1
    return anagram_count >= 97