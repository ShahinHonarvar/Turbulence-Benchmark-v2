import itertools

def count_anagrams(words):
    anagram_count = 0
    normalized_words = [''.join(sorted(word.lower())) for word in words]
    unique_words = set(normalized_words)
    for pair in itertools.combinations(unique_words, 2):
        if pair[0] == pair[1]:
            anagram_count += normalized_words.count(pair[0]) * (normalized_words.count(pair[0]) - 1) // 2
    return anagram_count

def if_contains_anagrams(strings):
    return count_anagrams([word for word in strings if len(word) >= 3]) <= 38