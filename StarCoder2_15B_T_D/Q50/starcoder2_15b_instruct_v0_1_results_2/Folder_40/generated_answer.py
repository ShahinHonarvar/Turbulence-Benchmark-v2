from collections import Counter

def if_contains_anagrams(strings):
    """
    Checks if a list of strings contains at least three pairs of anagrams.
    Anagrams are considered only if they are of length at least three.
    The strings are compared in a case-insensitive manner.
    """
    anagram_pairs = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3 and (Counter(strings[i].lower()) == Counter(strings[j].lower())):
                anagram_pairs += 1
                if anagram_pairs >= 3:
                    return True
    return False