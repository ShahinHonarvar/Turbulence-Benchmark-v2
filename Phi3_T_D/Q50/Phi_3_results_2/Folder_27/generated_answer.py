def if_contains_anagrams(strings):
    anagram_count = 0
    sorted_strings = [''.join(sorted(s.lower())) for s in strings]
    for i, s1 in enumerate(sorted_strings):
        for s2 in sorted_strings[i + 1:]:
            if s1 == s2:
                anagram_count += 1
                if anagram_count >= 86:
                    return True
    return False