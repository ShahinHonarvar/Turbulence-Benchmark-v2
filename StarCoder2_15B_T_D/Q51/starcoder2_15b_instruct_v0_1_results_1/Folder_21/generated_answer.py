def if_contains_anagrams(input_list):
    anagram_pairs = {}
    for string in input_list:
        canonical_form = ''.join(sorted(string.lower()))
        if len(canonical_form) >= 3 and canonical_form not in anagram_pairs:
            if canonical_form in anagram_pairs:
                anagram_pairs[canonical_form] += 1
            else:
                anagram_pairs[canonical_form] = 1
    return len(anagram_pairs) <= 26