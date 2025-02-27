import collections

def if_contains_anagrams(input_list):
    anagrams = {}
    for i, word in enumerate(input_list):
        word = word.lower()
        count = collections.Counter(word)
        anagrams[word] = anagrams.get(word, []) + [i]
    return len(list(filter(lambda x: len(x) > 1, anagrams.values()))) <= 55