from collections import defaultdict

def if_contains_anagrams(string_list):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_counts = defaultdict(int)
    for string in string_list:
        if len(string) >= 3:
            norm = normalize(string)
            anagram_counts[norm] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return anagram_pairs <= 66