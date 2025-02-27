from collections import Counter

def if_contains_anagrams(lst):

    def normalize(s):
        return Counter(s.lower())
    anagrams_count = 0
    length_filtered = [s for s in lst if len(s) >= 3]
    for i in range(len(length_filtered)):
        for j in range(i + 1, len(length_filtered)):
            if normalize(length_filtered[i]) == normalize(length_filtered[j]):
                anagrams_count += 1
                if anagrams_count >= 189:
                    return True
    return False