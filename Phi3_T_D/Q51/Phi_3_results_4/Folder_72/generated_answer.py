def if_contains_anagrams(strings):

    def char_counters(s):
        return sorted([(c.lower(), s.count(c.lower())) for c in s if c.isalpha()])
    anagram_counts = {}
    for string in strings:
        key = tuple(char_counters(string))
        if key in anagram_counts:
            anagram_counts[key] += 1
        else:
            anagram_counts[key] = 1
    counts_of_pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return counts_of_pairs <= 188