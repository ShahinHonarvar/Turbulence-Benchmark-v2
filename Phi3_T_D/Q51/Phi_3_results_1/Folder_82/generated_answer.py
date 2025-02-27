from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        return len(str1) == len(str2) and sorted(str1.lower()) == sorted(str2.lower())
    anagram_counts = defaultdict(int)
    for string in strings:
        if len(string) < 3:
            continue
        anagram_key = ''.join(sorted(string.lower()))
        anagram_counts[anagram_key] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return anagram_pairs <= 40