def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        key = ''.join(sorted(string.lower()))
        if len(key) >= 3:
            if key in anagrams:
                anagrams[key].append(string)
            else:
                anagrams[key] = [string]
    count = 0
    for anagram in anagrams.values():
        n = len(anagram)
        count += n * (n - 1) // 2
    return count <= 98