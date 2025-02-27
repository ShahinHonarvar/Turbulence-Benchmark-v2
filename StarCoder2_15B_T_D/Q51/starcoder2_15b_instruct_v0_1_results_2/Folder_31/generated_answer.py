def if_contains_anagrams(strings):
    anagram_counts = {}
    for string in strings:
        key = ''.join(sorted(string.lower()))
        if len(key) >= 3:
            anagram_counts[key] = anagram_counts.get(key, 0) + 1
    return max(anagram_counts.values(), default=0) <= 65