def if_contains_anagrams(strings):
    anagram_groups = {}
    for string in strings:
        key = ''.join(sorted(string.lower()))
        if len(key) >= 3:
            if key in anagram_groups:
                anagram_groups[key].append(string)
            else:
                anagram_groups[key] = [string]
    num_anagram_groups = len(anagram_groups)
    return num_anagram_groups <= 26