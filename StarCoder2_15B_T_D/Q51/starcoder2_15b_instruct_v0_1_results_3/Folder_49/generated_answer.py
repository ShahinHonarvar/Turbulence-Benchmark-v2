from collections import Counter

def if_contains_anagrams(strings):
    anagram_pairs = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                anagram_pairs += 1
                if anagram_pairs > 10:
                    return False
    return True

def is_anagram(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    if len(str1) != len(str2):
        return False
    counter1 = Counter((c for c in str1 if c.isalpha()))
    counter2 = Counter((c for c in str2 if c.isalpha()))
    return counter1 == counter2