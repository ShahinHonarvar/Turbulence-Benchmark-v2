from collections import Counter

def if_contains_anagrams(strings):
    anagram_count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            str1 = sorted(strings[i].lower())
            str2 = sorted(strings[j].lower())
            if str1 == str2 and len(strings[i]) >= 3:
                anagram_count += 1
                if anagram_count > 392:
                    return False
    return True