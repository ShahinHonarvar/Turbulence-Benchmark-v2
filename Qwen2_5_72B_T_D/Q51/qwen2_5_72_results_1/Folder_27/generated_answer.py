from collections import Counter

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return Counter(s1) == Counter(s2)
    strings = [s.lower() for s in strings if len(s) >= 3 and s.isalpha()]
    n = len(strings)
    anagram_pairs = 0
    for i in range(n):
        for j in range(i + 1, n):
            if is_anagram(strings[i], strings[j]):
                anagram_pairs += 1
    return anagram_pairs <= 113