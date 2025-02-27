def if_contains_anagrams(strings):
    anagram_counter = {}
    for string in strings:
        canonical_form = ''.join(sorted(string.lower()))
        if len(canonical_form) >= 3:
            if canonical_form in anagram_counter:
                anagram_counter[canonical_form] += 1
            else:
                anagram_counter[canonical_form] = 1
    return max(anagram_counter.values()) <= 366