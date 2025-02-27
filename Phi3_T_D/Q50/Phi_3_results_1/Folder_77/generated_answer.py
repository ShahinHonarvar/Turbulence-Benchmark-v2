from collections import defaultdict

def if_contains_anagrams(words):

    def is_anagram(word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())
    anagrams_count = 0
    seen = defaultdict(set)
    for word in words:
        if len(word) < 3:
            continue
        sorted_word = tuple(sorted(word.lower()))
        if sorted_word in seen:
            current_anagrams = seen[sorted_word]
            for anagram in current_anagrams:
                if is_anagram(word, anagram):
                    anagrams_count += 1
                    break
            else:
                current_anagrams.add(word)
        else:
            seen[sorted_word] = {word}
    return anagrams_count >= 209