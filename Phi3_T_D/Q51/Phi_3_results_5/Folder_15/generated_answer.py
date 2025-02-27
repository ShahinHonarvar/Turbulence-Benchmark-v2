def if_contains_anagrams(strings):

    def char_count(s, case_insensitive=True):
        counts = {}
        for char in s:
            if case_insensitive:
                char = char.lower()
            if char.isalpha():
                counts[char] = counts.get(char, 0) + 1
        return counts

    def sort_str(s, case_insensitive=True):
        return ''.join(sorted(filter(str.isalpha, s))).lower() if case_insensitive else ''.join(sorted(filter(str.isalpha, s)))
    sorted_strings = [sort_str(s, case_insensitive=True) for s in strings]
    unique_sorted = set(sorted_strings)
    anagram_counts = 0
    for count in (sorted_strings.count(sorted) for sorted in unique_sorted if sorted_strings.count(sorted) > 1):
        anagram_counts += count * (count - 1) // 2
    return anagram_counts <= 20