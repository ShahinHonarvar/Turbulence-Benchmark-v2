def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_count = {}
    for string in strings:
        if len(string) >= 3 and string.isalpha():
            normalized = normalize(string)
            anagram_count[normalized] = anagram_count.get(normalized, 0) + 1
    pairs = sum((count * (count - 1) // 2 for count in anagram_count.values()))
    return pairs <= 9