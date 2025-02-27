def if_contains_anagrams(strings):

    def are_anagrams(s1, s2):
        return sorted(s1) == sorted(s2)
    strings = [s.lower() for s in strings if s.isalpha() and len(s) >= 3]
    anagram_count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if are_anagrams(strings[i], strings[j]):
                anagram_count += 1
                if anagram_count > 11:
                    return False
    return True