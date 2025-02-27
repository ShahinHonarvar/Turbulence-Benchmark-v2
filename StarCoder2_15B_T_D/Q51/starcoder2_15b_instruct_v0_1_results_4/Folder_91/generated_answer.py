def if_contains_anagrams(strings):
    anagram_counts = {}
    for string in strings:
        canonical_form = ''.join(sorted(string.lower()))
        if canonical_form in anagram_counts:
            anagram_counts[canonical_form] += 1
        else:
            anagram_counts[canonical_form] = 1
    anagram_counts_list = list(anagram_counts.values())
    num_anagrams = sum((1 for count in anagram_counts_list if count > 1))
    return num_anagrams <= 88