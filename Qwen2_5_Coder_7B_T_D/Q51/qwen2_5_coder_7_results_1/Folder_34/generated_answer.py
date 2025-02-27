from collections import Counter

def if_contains_anagrams(words):

    def is_anagram(s1, s2):
        return Counter(s1.lower()) == Counter(s2.lower())
    n = len(words)
    for i in range(n):
        for j in range(i + 1, n):
            if len(words[i]) >= 3 and len(words[j]) >= 3 and is_anagram(words[i], words[j]):
                return False
    return True