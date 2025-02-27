from collections import defaultdict

def is_anagram(str1, str2):
    return sorted(str1.lower()) == sorted(str2.lower())

def if_contains_anagrams(strings_list):
    anagram_counts = defaultdict(int)
    for s in strings_list:
        if len(s) >= 3:
            t = ''.join(sorted(s.lower()))
            anagram_counts[t] += 1
    num_pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return num_pairs <= 188