def if_contains_anagrams(lst):
    anagram_counter = {}
    for s in lst:
        canonical_form = ''.join(sorted(s.lower()))
        if len(canonical_form) >= 3:
            if canonical_form in anagram_counter:
                anagram_counter[canonical_form] += 1
            else:
                anagram_counter[canonical_form] = 1
    return max(anagram_counter.values()) <= 255