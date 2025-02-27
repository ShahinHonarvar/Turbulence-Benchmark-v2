from collections import Counter

def if_contains_anagrams(strings):

    def are_anagrams(s1, s2):
        return Counter(s1) == Counter(s2)
    count = 0
    strings = [s.lower() for s in strings if len(s) >= 3]
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if are_anagrams(strings[i], strings[j]):
                count += 1
    return count <= 47