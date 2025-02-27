def if_contains_anagrams(strings):
    anagram_pairs = {}
    for string in strings:
        string = ''.join((c for c in string.lower() if c.isalpha()))
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string))
            anagram_pairs[sorted_string] = anagram_pairs.get(sorted_string, 0) + 1
    return len(anagram_pairs) <= 29