def if_contains_anagrams(strings):
    anagram_groups = {}
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3 and sorted_string.isalpha():
            if sorted_string in anagram_groups:
                anagram_groups[sorted_string].append(string)
            else:
                anagram_groups[sorted_string] = [string]
    anagram_pairs = sum((len(group) - 1 for group in anagram_groups.values()))
    return anagram_pairs <= 61