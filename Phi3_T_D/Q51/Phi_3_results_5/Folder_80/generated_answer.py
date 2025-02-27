def if_contains_anagrams(strings):

    def count_chars(s):
        count = [0] * 26
        for c in s:
            count[ord(c.lower()) - ord('a')] += 1
        return tuple(count)
    string_counts = {}
    for s in strings:
        if len(s) < 3:
            continue
        s_lower = s.lower()
        s_count = count_chars(s_lower)
        if s_count in string_counts:
            string_counts[s_count].append(s_lower)
        else:
            string_counts[s_count] = [s_lower]
    anagram_pairs = sum((len(strings) * (len(strings) - 1) // 2 for strings in string_counts.values() if len(strings) > 1))
    return anagram_pairs <= 255