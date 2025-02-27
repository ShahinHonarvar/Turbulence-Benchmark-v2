def if_contains_anagrams(input_list):
    anagrams = {}
    for string in input_list:
        key = ''.join(sorted(string.lower()))
        if len(key) >= 3:
            if key in anagrams:
                anagrams[key] += 1
            else:
                anagrams[key] = 1
    return len(anagrams) <= 68