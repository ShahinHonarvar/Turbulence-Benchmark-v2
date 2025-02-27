def if_contains_anagrams(strings):

    def to_lower(s):
        return s.lower()

    def is_anagram(s1, s2):
        return sorted(s1) == sorted(s2)
    strings = list(map(to_lower, strings))
    anagram_pairs = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3 and is_anagram(strings[i], strings[j]):
                anagram_pairs += 1
                if anagram_pairs > 24:
                    return False
    return True