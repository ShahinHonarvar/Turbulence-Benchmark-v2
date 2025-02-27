from collections import Counter

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return Counter(s1.lower()) == Counter(s2.lower())
    n = len(strings)
    for i in range(n):
        for j in range(i + 1, n):
            if is_anagram(strings[i], strings[j]):
                return True
    return False