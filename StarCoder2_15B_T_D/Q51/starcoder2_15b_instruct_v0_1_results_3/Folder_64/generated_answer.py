def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        key = ''.join(sorted(string.lower()))
        if len(key) >= 3 and key.isalpha():
            anagrams[key] = anagrams.get(key, 0) + 1
    return len(anagrams) <= 59