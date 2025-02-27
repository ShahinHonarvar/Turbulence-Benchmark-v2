from collections import defaultdict

def if_contains_anagrams(strings):
    sorted_strings_by_length = sorted((s.lower() for s in strings if len(s) >= 3), key=sorted)
    grouped_anagrams = defaultdict(int)
    for sorted_string in sorted_strings_by_length:
        grouped_anagrams[tuple(sorted_string)] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in grouped_anagrams.values()))
    return anagram_pairs >= 89