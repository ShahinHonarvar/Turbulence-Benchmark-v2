from collections import defaultdict

def if_contains_anagrams(str_list):
    count = 0
    str_length = 3
    anagram_map = defaultdict(list)
    for s in str_list:
        if len(s) >= str_length:
            cleaned = ''.join(sorted(s.lower()))
            anagram_map[cleaned].append(s)
    for anagrams in anagram_map.values():
        if len(anagrams) >= 2:
            count += len(anagrams) * (len(anagrams) - 1) // 2
    return count >= 22