from collections import Counter

def if_contains_anagrams(strings):
    anagram_pairs = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                str1 = Counter(strings[i].lower())
                str2 = Counter(strings[j].lower())
                if str1 == str2:
                    anagram_pairs += 1
                    if anagram_pairs > 10:
                        return False
    return True