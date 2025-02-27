def if_contains_anagrams(strings):
    anagram_groups = {}
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if sorted_string not in anagram_groups:
            anagram_groups[sorted_string] = [string]
        else:
            anagram_groups[sorted_string].append(string)
    anagram_counts = [len(group) for group in anagram_groups.values()]
    anagram_counts.sort(reverse=True)
    return sum(anagram_counts) <= 50