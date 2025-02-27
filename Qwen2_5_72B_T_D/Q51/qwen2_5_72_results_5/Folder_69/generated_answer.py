def if_contains_anagrams(strings):

    def normalize(string):
        return ''.join(sorted(string.lower()))
    anagram_counts = {}
    for string in strings:
        if len(string) >= 3 and string.isalpha():
            normalized = normalize(string)
            if normalized in anagram_counts:
                anagram_counts[normalized] += 1
            else:
                anagram_counts[normalized] = 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return anagram_pairs <= 58