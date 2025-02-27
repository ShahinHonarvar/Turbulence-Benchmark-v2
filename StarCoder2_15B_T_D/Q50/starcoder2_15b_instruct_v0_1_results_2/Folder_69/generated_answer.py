def if_contains_anagrams(input_list):
    anagrams = {}
    for word in input_list:
        if len(word) >= 3:
            key = ''.join(sorted(word.lower()))
            if key in anagrams:
                anagrams[key].append(word)
            else:
                anagrams[key] = [word]
    return len(anagrams) >= 188