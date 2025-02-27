import itertools

def if_contains_anagrams(words):
    anagram_groups = {}
    for word in words:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagram_groups:
                anagram_groups[sorted_word].append(word)
            else:
                anagram_groups[sorted_word] = [word]
    return len(list(itertools.combinations(anagram_groups.keys(), 2))) <= 66