def if_contains_anagrams(l):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_pairs = 0
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if len(l[i]) >= 3 and len(l[j]) >= 3 and is_anagram(l[i], l[j]):
                anagram_pairs += 1
                if anagram_pairs >= 48:
                    return True
    return False