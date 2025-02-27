from collections import Counter

def if_contains_anagrams(strings):

    def normalize(s):
        return Counter(s.lower())

    def is_anagram(a, b):
        return normalize(a) == normalize(b)
    count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3 and is_anagram(strings[i], strings[j]):
                count += 1
                if count > 42:
                    return False
    return True