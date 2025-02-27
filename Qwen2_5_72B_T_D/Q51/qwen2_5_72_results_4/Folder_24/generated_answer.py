from collections import Counter

def if_contains_anagrams(strings):
    anagram_pairs = set()
    for i, str1 in enumerate(strings):
        sorted_str1 = ''.join(sorted(str1.lower()))
        if len(sorted_str1) < 3:
            continue
        for str2 in strings[i + 1:]:
            sorted_str2 = ''.join(sorted(str2.lower()))
            if sorted_str1 == sorted_str2:
                anagram_pairs.add((str1, str2))
    return len(anagram_pairs) <= 96