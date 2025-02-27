def if_contains_anagrams(strings):
    char_sets = [{char.lower() for char in string} for string in strings]
    anagram_groups = {}
    for char_set in char_sets:
        if char_set in anagram_groups:
            anagram_groups[char_set].append(strings[char_sets.index(char_set)])
        else:
            anagram_groups[char_set] = [strings[char_sets.index(char_set)]]
    return len([group for group in anagram_groups.values() if len(group) >= 3]) >= 65