def if_contains_anagrams(lst):
    anagram_pairs = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if is_anagram(lst[i], lst[j]):
                anagram_pairs += 1
                if anagram_pairs > 36:
                    return False
    return True

def is_anagram(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    if len(str1) >= 3 and len(str2) >= 3:
        return sorted(str1) == sorted(str2)
    else:
        return False