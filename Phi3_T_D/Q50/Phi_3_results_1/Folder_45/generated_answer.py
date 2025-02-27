def if_contains_anagrams(word_list):

    def clean_word(word):
        return ''.join(sorted(word.lower()))
    anagrams = {}
    for word in word_list:
        cleaned_word = clean_word(word)
        anagrams.setdefault(cleaned_word, []).append(word)
    count = sum((1 for group in anagrams.values() if len(group) > 1 and len(group[0]) >= 3))
    return count >= 277