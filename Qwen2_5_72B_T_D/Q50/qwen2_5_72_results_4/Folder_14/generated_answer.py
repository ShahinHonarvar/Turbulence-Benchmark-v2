def if_contains_anagrams(strings):

    def are_anagrams(s1, s2):
        return sorted(s1) == sorted(s2)
    strings = [s.lower() for s in strings if len(s) >= 3]
    anagram_pairs = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if are_anagrams(strings[i], strings[j]):
                anagram_pairs += 1
                if anagram_pairs >= 22:
                    return True
    return False