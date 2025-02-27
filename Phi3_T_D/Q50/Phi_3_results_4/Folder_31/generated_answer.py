from collections import defaultdict

def if_contains_anagrams(strings):
    length_map = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            length_map[sorted_string].append(string)
    count_pairs = 0
    for anagrams in length_map.values():
        n = len(anagrams)
        count_pairs += n * (n - 1) // 2
    return count_pairs >= 68