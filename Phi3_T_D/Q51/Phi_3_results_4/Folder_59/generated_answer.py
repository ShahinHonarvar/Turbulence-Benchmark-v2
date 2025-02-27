def if_contains_anagrams(words):

    def count_letters(word):
        letter_count = {}
        for letter in word:
            letter_count[letter.lower()] = letter_count.get(letter.lower(), 0) + 1
        return letter_count
    sorted_words = [''.join(sorted(word.lower())) for word in words if len(word) >= 3]
    anagram_counts = {}
    for word in sorted_words:
        if word in anagram_counts:
            anagram_counts[word] += 1
        else:
            anagram_counts[word] = 1
    number_of_pairs = sum((1 for count in anagram_counts.values() if count > 1))
    return number_of_pairs <= 15