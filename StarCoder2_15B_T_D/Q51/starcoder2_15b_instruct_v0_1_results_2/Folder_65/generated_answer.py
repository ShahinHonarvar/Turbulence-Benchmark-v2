def if_contains_anagrams(input_list):
    anagrams = {}
    for s in input_list:
        s = s.lower()
        if len(s) >= 3:
            key = ''.join(sorted(s))
            if key in anagrams:
                anagrams[key].append(s)
            else:
                anagrams[key] = [s]
    return len(anagrams) <= 72