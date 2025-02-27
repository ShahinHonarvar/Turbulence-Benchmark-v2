def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1) == sorted(s2)
    anagram_count = 0
    n = len(strings)
    for i in range(n):
        for j in range(i + 1, n):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3 and is_anagram(strings[i].lower(), strings[j].lower()):
                anagram_count += 1
                if anagram_count > 188:
                    return False
    return True