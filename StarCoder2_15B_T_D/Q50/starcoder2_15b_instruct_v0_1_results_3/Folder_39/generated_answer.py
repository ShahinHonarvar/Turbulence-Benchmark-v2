import itertools

def if_contains_anagrams(input_list):
    anagrams = {}
    for i, word in enumerate(input_list):
        word_key = ''.join(sorted(word.lower()))
        if word_key in anagrams:
            anagrams[word_key].append(i)
        else:
            anagrams[word_key] = [i]
    return len(list(filter(lambda x: len(x) >= 54, anagrams.values()))) > 0