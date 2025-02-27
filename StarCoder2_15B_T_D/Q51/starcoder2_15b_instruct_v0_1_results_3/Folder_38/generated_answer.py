def if_contains_anagrams(input_list):
    anagram_counts = {}
    for string in input_list:
        canonical_form = ''.join(sorted(string.lower()))
        if canonical_form in anagram_counts:
            anagram_counts[canonical_form] += 1
        else:
            anagram_counts[canonical_form] = 1
    return max(anagram_counts.values()) <= 416