def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))

    def is_valid_pair(a, b):
        return len(a) >= 3 and len(b) >= 3
    anagram_pairs = 0
    checked_pairs = set()
    for i, string1 in enumerate(strings):
        for string2 in strings[i + 1:]:
            if (string1, string2) in checked_pairs or (string2, string1) in checked_pairs:
                continue
            if normalize(string1) == normalize(string2) and is_valid_pair(string1, string2):
                anagram_pairs += 1
                checked_pairs.add((string1, string2))
                checked_pairs.add((string2, string1))
    return anagram_pairs <= 43