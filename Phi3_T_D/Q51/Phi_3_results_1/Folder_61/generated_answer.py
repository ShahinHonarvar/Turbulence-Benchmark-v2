def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower())).rstrip('0123456789')
    unique_words = {}
    for word in words:
        key = normalize(word)
        if key in unique_words and len(word) >= 3:
            unique_words[key].append(word)
    anagram_pairs = sum((len(word_list) * (len(word_list) - 1) // 2 for word_list in unique_words.values() if len(word_list) > 1))
    return anagram_pairs <= 50