def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_pairs = set()
    for string in strings:
        if len(string) >= 3 and string.isalpha():
            norm = normalize(string)
            for other in strings:
                if string != other and len(other) >= 3 and other.isalpha() and (normalize(other) == norm):
                    if (string, other) not in anagram_pairs and (other, string) not in anagram_pairs:
                        anagram_pairs.add((string, other))
    return len(anagram_pairs) <= 48