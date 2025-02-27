def if_contains_anagrams(strings):
    sorted_strings = []
    for string in strings:
        string = string.lower()
        string = ''.join((c for c in string if c.isalpha()))
        sorted_string = ''.join(sorted(string))
        sorted_strings.append(sorted_string)
    anagram_counts = {}
    for sorted_string in sorted_strings:
        if sorted_string in anagram_counts:
            anagram_counts[sorted_string] += 1
        else:
            anagram_counts[sorted_string] = 1
    return max(anagram_counts.values()) <= 206