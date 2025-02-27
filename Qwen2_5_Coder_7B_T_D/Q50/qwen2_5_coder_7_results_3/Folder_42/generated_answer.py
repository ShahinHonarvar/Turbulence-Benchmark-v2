from collections import Counter

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return Counter(s1) == Counter(s2)
    strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                return True
    return False