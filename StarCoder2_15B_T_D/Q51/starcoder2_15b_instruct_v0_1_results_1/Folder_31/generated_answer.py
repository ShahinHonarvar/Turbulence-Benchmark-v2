def if_contains_anagrams(strings):
    anagram_counts = {}
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            if sorted_string in anagram_counts:
                anagram_counts[sorted_string] += 1
            else:
                anagram_counts[sorted_string] = 1
    return max(anagram_counts.values()) <= 65