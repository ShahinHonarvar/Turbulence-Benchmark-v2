def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        key = ''.join(sorted(word.lower()))
        if key in anagrams:
            anagrams[key].append(word)
        else:
            anagrams[key] = [word]
    return len(anagrams) >= 89