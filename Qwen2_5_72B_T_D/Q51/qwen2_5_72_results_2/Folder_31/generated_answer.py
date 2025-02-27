def if_contains_anagrams(strings):

    def to_tuple(s):
        return tuple(sorted(s.lower()))
    anagram_count = {}
    for string in strings:
        if len(string) >= 3 and string.isalpha():
            key = to_tuple(string)
            anagram_count[key] = anagram_count.get(key, 0) + 1
    pairs = sum((count * (count - 1) // 2 for count in anagram_count.values()))
    return pairs <= 65