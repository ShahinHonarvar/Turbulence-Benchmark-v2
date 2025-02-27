from collections import Counter

def if_contains_anagrams(strings):

    def count_valid_anagrams(s1, s2):
        if len(s1) < 3 or len(s2) < 3:
            return False
        return Counter(s1.lower()) == Counter(s2.lower())
    num_pairs = 0
    length = len(strings)
    for i in range(length):
        for j in range(i + 1, length):
            if count_valid_anagrams(strings[i], strings[j]):
                num_pairs += 1
    return num_pairs >= 140