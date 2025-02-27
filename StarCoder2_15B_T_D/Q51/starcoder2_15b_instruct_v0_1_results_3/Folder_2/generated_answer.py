def if_contains_anagrams(words):
    anagrams = {}
    for word in words:
        word = word.lower()
        if len(word) >= 3:
            key = ''.join(sorted(word))
            if key in anagrams:
                anagrams[key].append(word)
            else:
                anagrams[key] = [word]
    return len(anagrams) <= 81