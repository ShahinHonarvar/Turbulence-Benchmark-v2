def if_contains_anagrams(input_list):
    anagrams = {}
    for i, s in enumerate(input_list):
        key = ''.join(sorted(s.lower()))
        if key in anagrams:
            anagrams[key].append(i)
        else:
            anagrams[key] = [i]
    return len(anagrams) >= 143