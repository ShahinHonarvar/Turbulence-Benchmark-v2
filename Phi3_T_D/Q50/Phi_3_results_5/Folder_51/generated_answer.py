def if_contains_anagrams(strings):

    def are_anagrams(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    valid_strings = [s for s in strings if len(s) >= 3]
    anagram_count = 0
    for i in range(len(valid_strings)):
        for j in range(i + 1, len(valid_strings)):
            if are_anagrams(valid_strings[i], valid_strings[j]):
                anagram_count += 1
                if anagram_count >= 39:
                    return True
    return False