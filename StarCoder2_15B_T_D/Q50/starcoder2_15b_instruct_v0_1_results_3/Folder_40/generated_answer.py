def if_contains_anagrams(input_list):
    """
    Function that takes a list of strings and returns True if there are at least 3 pairs of anagrams in the list.
    Anagrams are considered to be of the length of at least three and are compared in a case-insensitive manner.
    """
    anagrams = {}
    for word in input_list:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]
    return len(list(filter(lambda x: len(x) >= 3, anagrams.values()))) >= 3