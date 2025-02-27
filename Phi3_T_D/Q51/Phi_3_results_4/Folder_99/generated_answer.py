from collections import defaultdict

def if_contains_anagrams(strings):

    def count_letters(word):
        letter_count = defaultdict(int)
        for letter in word:
            letter_count[letter.lower()] += 1
        return tuple(sorted(letter_count.items()))
    pair_count = 0
    letter_counts = {}
    for string in strings:
        word_length = len(string)
        if word_length >= 3:
            letter_count = count_letters(string)
            if letter_count in letter_counts:
                pair_count += letter_counts[letter_count]
                if pair_count > 92:
                    return False
                letter_counts[letter_count] += 1
            else:
                letter_counts[letter_count] = 1
    return True