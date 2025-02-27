from collections import defaultdict

def if_contains_anagrams(strings_list):
    anagrams = defaultdict(int)
    for string in strings_list:
        if len(string) >= 3:
            sorted_str = ''.join(sorted(string.lower()))
            anagrams[sorted_str] += 1
    count_pairs = sum((v // 2 for v in anagrams.values()))
    return count_pairs >= 189