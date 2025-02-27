def if_contains_anagrams(string_list):
    clean_list = [string.lower() for string in string_list if len(string) >= 3]
    sorted_list = [''.join(sorted(string)) for string in clean_list]
    anagram_counts = {}
    for sorted_string in sorted_list:
        if sorted_string in anagram_counts:
            anagram_counts[sorted_string] += 1
        else:
            anagram_counts[sorted_string] = 1
    return any((count >= 30 for count in anagram_counts.values()))