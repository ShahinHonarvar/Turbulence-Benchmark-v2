def if_contains_anagrams(strings):
    anagram_pairs = []
    processed_lengths = set()
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if sorted_string in strings and len(string) >= 3 and (len(string) not in processed_lengths):
            anagram_pairs.append((string, sorted_string))
            processed_lengths.add(len(string))
    return len(anagram_pairs) >= 178