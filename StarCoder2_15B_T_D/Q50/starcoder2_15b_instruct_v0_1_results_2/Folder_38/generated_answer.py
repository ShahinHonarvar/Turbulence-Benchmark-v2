import itertools

def if_contains_anagrams(words):
    anagrams = {}
    for word in words:
        word_key = ''.join(sorted(word.lower()))
        if word_key not in anagrams:
            anagrams[word_key] = [word]
        else:
            anagrams[word_key].append(word)
    return len(anagrams) >= 24 and any((len(v) >= 3 for v in anagrams.values()))