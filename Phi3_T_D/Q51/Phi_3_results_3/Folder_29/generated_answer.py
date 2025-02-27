from collections import defaultdict

def if_contains_anagrams(strings):
    letter_anagrams_count = defaultdict(int)
    clean_strings = [''.join(filter(str.isalpha, s)).lower() for s in strings]
    for string in clean_strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string))
            letter_anagrams_count[sorted_string] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in letter_anagrams_count.values()))
    return anagram_pairs <= 318