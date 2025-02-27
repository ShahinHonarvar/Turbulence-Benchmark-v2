def if_contains_anagrams(strings):
    count = 0
    anagrams = {}
    for string in strings:
        key = ''.join(sorted(string.lower()))
        if key not in anagrams:
            anagrams[key] = [string]
        else:
            anagrams[key].append(string)
    for key in anagrams:
        if len(anagrams[key]) >= 3:
            count += len(anagrams[key]) * (len(anagrams[key]) - 1) // 2
    return count >= 72