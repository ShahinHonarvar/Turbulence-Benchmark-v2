def if_contains_anagrams(strings):

    def are_anagrams(s1, s2):
        return len(s1) == len(s2) and sorted(s1.lower()) == sorted(s2.lower())
    anagram_count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and are_anagrams(strings[i], strings[j]):
                anagram_count += 1
                if anagram_count >= 65:
                    return True
    return False