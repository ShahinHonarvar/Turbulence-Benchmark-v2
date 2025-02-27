from collections import Counter
    import string

def if_contains_anagrams(strings):

    def is_valid_anagram_pair(s1, s2):
        if len(s1) < 3 or len(s2) < 3:
            return False
        return Counter(s1) == Counter(s2)
    strings = [s.lower() for s in strings if set(s).issubset(set(string.ascii_letters))]
    anagram_pairs = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_valid_anagram_pair(strings[i], strings[j]):
                anagram_pairs += 1
    return anagram_pairs <= 81