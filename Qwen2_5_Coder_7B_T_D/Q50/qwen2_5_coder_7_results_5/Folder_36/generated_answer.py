from collections import Counter

def if_contains_anagrams(words):

    def are_anagrams(s1, s2):
        return Counter(s1) == Counter(s2)
    n = len(words)
    for i in range(n):
        for j in range(i + 1, n):
            if len(words[i]) >= 3 and len(words[j]) >= 3 and (words[i].lower() != words[j].lower()) and are_anagrams(words[i], words[j]):
                return True
    return False