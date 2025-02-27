import itertools

def if_contains_anagrams(words):
    filtered_words = [word for word in words if len(word) >= 3 and word.isalpha()]
    sorted_words = [''.join(sorted(word.lower())) for word in filtered_words]
    anagram_groups = {}
    for word, sorted_word in zip(filtered_words, sorted_words):
        if sorted_word in anagram_groups:
            anagram_groups[sorted_word].append(word)
        else:
            anagram_groups[sorted_word] = [word]
    anagram_pairs = [(word1, word2) for sorted_word, words in anagram_groups.items() for word1, word2 in itertools.combinations(words, 2)]
    return len(anagram_pairs) <= 79