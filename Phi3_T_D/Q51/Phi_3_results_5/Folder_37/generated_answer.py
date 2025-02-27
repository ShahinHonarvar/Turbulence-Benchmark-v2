from collections import Counter

def if_contains_anagrams(strings):

    def clean_and_encode(s):
        return ''.join(sorted(filter(str.isalpha, s.lower())))
    encoded_strings = [clean_and_encode(s) for s in strings]
    unique_encoded_strings = set(encoded_strings)
    anagram_counts = sum((1 for count in (encoded_strings.count(e) for e in unique_encoded_strings) if count > 1 and encoded_strings.count(e) >= 3))
    return anagram_counts * (anagram_counts - 1) // 2 <= 206