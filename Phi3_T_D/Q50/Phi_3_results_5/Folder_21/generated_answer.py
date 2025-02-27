from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())

    def count_anagrams(words):
        anagrams_count = 0
        sorted_words = defaultdict(list)
        for word in words:
            if len(word) >= 3:
                sorted_word = tuple(sorted(word))
                if sorted_words[sorted_word]:
                    anagrams_count += len(sorted_words[sorted_word])
                    sorted_words[sorted_word] = []
                else:
                    sorted_words[sorted_word].append(word)
        return anagrams_count
    anagrams_pairs_count = count_anagrams(strings)
    return anagrams_pairs_count >= 136