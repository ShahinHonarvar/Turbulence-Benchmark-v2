import itertools

def if_contains_anagrams(words):
    anagrams = {}
    for word in words:
        key = ''.join(sorted(word.lower()))
        if len(key) >= 3:
            if key in anagrams:
                anagrams[key].append(word)
            else:
                anagrams[key] = [word]
    return len(list(itertools.combinations(anagrams.values(), 2))) <= 18