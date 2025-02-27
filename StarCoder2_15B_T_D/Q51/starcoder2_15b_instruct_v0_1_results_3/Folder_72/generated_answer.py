import itertools

def if_contains_anagrams(words):
    anagrams = {}
    for word in words:
        word = word.lower()
        key = ''.join(sorted(word))
        if len(word) >= 3:
            if key in anagrams:
                anagrams[key].append(word)
            else:
                anagrams[key] = [word]
    return len(list(itertools.combinations(anagrams.values(), 2))) <= 188