def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))

    def count_anagrams(normalized_strings):
        anagram_count = {}
        for s in normalized_strings:
            anagram_count[s] = anagram_count.get(s, 0) + 1
        return sum((count * (count - 1) // 2 for count in anagram_count.values()))
    normalized_strings = [normalize(s) for s in strings if len(s) >= 3]
    return count_anagrams(normalized_strings) <= 60