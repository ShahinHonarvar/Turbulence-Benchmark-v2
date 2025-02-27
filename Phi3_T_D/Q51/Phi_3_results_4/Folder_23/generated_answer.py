def if_contains_anagrams(string_list):
    sorted_strings = [''.join(sorted(word.lower())) for word in string_list if len(word) >= 3]
    anagram_counts = {}
    for sorted_str in sorted_strings:
        if sorted_str in anagram_counts:
            anagram_counts[sorted_str] += 1
            if anagram_counts[sorted_str] > 51:
                return False
        else:
            anagram_counts[sorted_str] = 1
    return True