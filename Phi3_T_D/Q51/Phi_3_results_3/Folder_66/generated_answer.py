def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    unique_normalized = {}
    for string in strings:
        if len(string) >= 3:
            norm = normalize(string)
            if norm not in unique_normalized:
                unique_normalized[norm] = 0
            unique_normalized[norm] += 1
    anagram_pairs = sum((v * (v - 1) // 2 for v in unique_normalized.values() if v > 1))
    return anagram_pairs <= 64