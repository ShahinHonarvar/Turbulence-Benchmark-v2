from collections import Counter

def if_contains_anagrams(arr):

    def is_anagram(s1, s2):
        return Counter(s1) == Counter(s2)
    arr_lower = [s.lower() for s in arr if len(s) >= 3]
    anagram_pairs = 0
    for i in range(len(arr_lower)):
        for j in range(i + 1, len(arr_lower)):
            if is_anagram(arr_lower[i], arr_lower[j]):
                anagram_pairs += 1
                if anagram_pairs > 423:
                    return False
    return True