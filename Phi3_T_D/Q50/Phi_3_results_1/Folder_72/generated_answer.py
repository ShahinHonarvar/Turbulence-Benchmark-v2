def if_contains_anagrams(strings):

    def make_anagram_key(s):
        return ''.join(sorted(s.lower()))
    filtered_strings = [s for s in strings if len(s) >= 3]
    anagram_counts = {}
    for s in filtered_strings:
        key = make_anagram_key(s)
        if key in anagram_counts:
            anagram_counts[key] += 1
        else:
            anagram_counts[key] = 1
    return sum((1 for count in anagram_counts.values() if count * (count - 1) >= 54))