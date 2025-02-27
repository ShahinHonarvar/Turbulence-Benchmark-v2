from collections import defaultdict

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    unique_sorted_strings = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            normalized = normalize(string)
            unique_sorted_strings[normalized] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in unique_sorted_strings.values() if count > 1))
    return anagram_pairs <= 47