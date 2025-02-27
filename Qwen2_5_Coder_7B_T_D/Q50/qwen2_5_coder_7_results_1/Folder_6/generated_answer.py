from collections import Counter

def if_contains_anagrams(strs):

    def is_anagram(s1, s2):
        return Counter(s1.lower()) == Counter(s2.lower())
    anagram_pairs = 0
    n = len(strs)
    for i in range(n):
        for j in range(i + 1, n):
            if len(strs[i]) >= 3 and len(strs[j]) >= 3 and is_anagram(strs[i], strs[j]):
                anagram_pairs += 1
                if anagram_pairs >= 26:
                    return True
    return False