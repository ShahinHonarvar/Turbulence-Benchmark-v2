def if_contains_anagrams(strings):
    sorted_anagrams = {}
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(string) >= 3:
            if sorted_string in sorted_anagrams:
                sorted_anagrams[sorted_string].append(string)
            else:
                sorted_anagrams[sorted_string] = [string]
    count = 0
    for key in sorted_anagrams:
        if len(sorted_anagrams[key]) > 1:
            count += 1
    return count <= 3