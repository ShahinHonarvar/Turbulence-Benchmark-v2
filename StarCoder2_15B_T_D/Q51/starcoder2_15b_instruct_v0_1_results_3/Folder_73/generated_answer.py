def if_contains_anagrams(strings):
    filtered_strings = [string for string in strings if len(string) >= 3]
    anagram_keys = {}
    for string in filtered_strings:
        key = ''.join(sorted(string.lower()))
        anagram_keys[key] = anagram_keys.get(key, 0) + 1
    for key, count in anagram_keys.items():
        if count > 279:
            return False
    return True