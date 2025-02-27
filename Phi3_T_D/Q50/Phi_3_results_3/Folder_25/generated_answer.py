from collections import defaultdict

def if_contains_anagrams(strings):
    length_filter = defaultdict(list)
    for word in strings:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            length_filter[sorted_word].append(word)
    anagram_count = sum((len(anagrams) > 1 for anagrams in length_filter.values()))
    return anagram_count >= 14