def if_contains_anagrams(strings):

    def can_make_anagram_pair(s1, s2):
        s1, s2 = (s1.lower(), s2.lower())
        return len(s1) >= 3 and sorted(s1) == sorted(s2)
    anagram_count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if can_make_anagram_pair(strings[i], strings[j]):
                anagram_count += 1
                if anagram_count > 39:
                    return False
    return True