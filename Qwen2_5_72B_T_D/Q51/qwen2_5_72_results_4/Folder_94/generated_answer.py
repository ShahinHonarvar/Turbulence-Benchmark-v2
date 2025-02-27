from collections import Counter

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        if len(s1) < 3 or len(s2) < 3:
            return False
        return Counter(s1) == Counter(s2)
    strings = [s.lower() for s in strings]
    anagram_pairs = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                anagram_pairs += 1
    return anagram_pairs <= 181