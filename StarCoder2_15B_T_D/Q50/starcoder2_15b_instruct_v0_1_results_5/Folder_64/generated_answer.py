def if_contains_anagrams(string_list):
    anagrams = {}
    for string in string_list:
        key = ''.join(sorted(string.lower()))
        if key in anagrams:
            anagrams[key].append(string)
        else:
            anagrams[key] = [string]
    count = 0
    for key in anagrams:
        if len(anagrams[key]) >= 5:
            count += 1
    return count >= 5