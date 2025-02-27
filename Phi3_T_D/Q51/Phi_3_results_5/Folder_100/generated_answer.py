from collections import Counter

def if_contains_anagrams(strings_list):

    def normalize(word):
        return Counter(word.lower())

    def convert_anagrams(normalize_func):
        grouped = {}
        for string in strings_list:
            if len(string) < 3:
                continue
            norm_str = normalize_func(string)
            if norm_str in grouped:
                grouped[norm_str].append(string)
            else:
                grouped[norm_str] = [string]
        return grouped.values()
    anagram_groups = convert_anagrams(normalize)
    anagram_pairs = sum((1 for group in anagram_groups if len(group) >= 2))
    return anagram_pairs <= 98