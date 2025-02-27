def if_contains_anagrams(words):

    def is_anagram(s1, s2):
        s1 = s1.lower()
        s2 = s2.lower()
        s1 = ''.join((c for c in s1 if c.isalpha()))
        s2 = ''.join((c for c in s2 if c.isalpha()))
        return sorted(s1) == sorted(s2) and len(s1) >= 3
    anagram_pairs = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if is_anagram(words[i], words[j]):
                anagram_pairs += 1
                if anagram_pairs > 22:
                    return False
    return anagram_pairs <= 22