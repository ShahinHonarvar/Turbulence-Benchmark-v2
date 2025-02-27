from collections import defaultdict

def if_contains_anagrams(strings):
    count = 0
    anagrams = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            sorted_str = ''.join(sorted(string.lower()))
            anagrams[sorted_str].append(string)
    for sorted_str in anagrams:
        if len(anagrams[sorted_str]) > 1:
            count += len(anagrams[sorted_str]) * (len(anagrams[sorted_str]) - 1) // 2
    return count >= 29