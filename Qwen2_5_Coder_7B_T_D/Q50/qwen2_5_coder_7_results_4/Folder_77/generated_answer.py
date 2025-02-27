from collections import Counter

def if_contains_anagrams(words):

    def is_anagram(s1, s2):
        return Counter(s1) == Counter(s2)
    count = 0
    words = [word.lower() for word in words if len(word) >= 3]
    n = len(words)
    for i in range(n):
        for j in range(i + 1, n):
            if is_anagram(words[i], words[j]):
                count += 1
    return count >= 209