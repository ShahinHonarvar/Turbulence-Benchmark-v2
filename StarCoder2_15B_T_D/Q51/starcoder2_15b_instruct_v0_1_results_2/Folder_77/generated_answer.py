def if_contains_anagrams(strings):
    normalized_strings = [s.lower() for s in strings]
    sorted_strings = [''.join(sorted(s)) for s in normalized_strings]
    anagram_pairs = {}
    for i, sorted_string in enumerate(sorted_strings):
        if sorted_string in anagram_pairs:
            anagram_pairs[sorted_string].append(i)
        else:
            anagram_pairs[sorted_string] = [i]
    num_anagrams = sum((len(anagram_pairs[sorted_string]) - 1 for sorted_string in anagram_pairs))
    return num_anagrams <= 17