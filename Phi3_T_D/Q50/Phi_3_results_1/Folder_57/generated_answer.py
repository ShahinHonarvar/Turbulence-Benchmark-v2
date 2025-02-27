def if_contains_anagrams(strings):

    def count_letters(word):
        return {letter: word.lower().count(letter) for letter in set(word.lower())}
    filtered = filter(lambda s: len(s) >= 3, strings)
    sorted_strings = [sorted(count_letters(word), key=str.lower) for word in filtered]
    counter = {}
    for word in sorted_strings:
        word_signature = tuple(word.values())
        counter[word_signature] = counter.get(word_signature, 0) + 1
    return sum((count * (count - 1) // 2 for count in counter.values())) >= 50