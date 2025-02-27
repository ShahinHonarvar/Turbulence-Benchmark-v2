from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams_count = 0
    length_anagrams = defaultdict(list)
    for word in strings:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            length_anagrams[sorted_word].append(word)
            if len(length_anagrams[sorted_word]) > 1:
                anagrams_count += len(length_anagrams[sorted_word]) - 1
    return anagrams_count >= 20