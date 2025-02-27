from collections import Counter

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return Counter(s1.lower()) == Counter(s2.lower())
    anagram_pairs = 0
    strings = [word for word in strings if len(word) >= 3]
    n = len(strings)
    for i in range(n):
        for j in range(i + 1, n):
            if is_anagram(strings[i], strings[j]):
                anagram_pairs += 1
                if anagram_pairs > 18:
                    return False
    return True