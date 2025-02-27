def if_contains_anagrams(strings):
    processed_strings = [''.join((char for char in string.lower() if char.isalpha())) for string in strings]
    anagram_groups = {}
    for string in processed_strings:
        sorted_string = ''.join(sorted(string))
        if sorted_string not in anagram_groups:
            anagram_groups[sorted_string] = [string]
        else:
            anagram_groups[sorted_string].append(string)
    return len(anagram_groups) <= 257