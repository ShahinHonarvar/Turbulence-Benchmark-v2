from collections import defaultdict
import itertools
import string

def if_contains_anagrams(words):
    anagram_count = 0
    letter_counts = [defaultdict(int) for _ in range(52)]
    clean_words = [''.join(filter(str.isalpha, word)).lower() for word in words]
    for word in clean_words:
        if len(word) < 3:
            continue
        index = 0
        for letter in word:
            if letter in string.ascii_letters:
                letter_counts[string.ascii_letters.index(letter)][letter] += 1
                index += 1
        count_tuple = tuple((letter_counts[i][char] for i, char in enumerate(string.ascii_letters)))
        letter_counts = letter_counts[len(count_tuple):]
        letter_counts.append(defaultdict(int))
        seen = set()
        for i in range(len(clean_words)):
            if clean_words[i] == word:
                continue
            current_count_tuple = tuple((letter_counts[i][char] for i, char in enumerate(string.ascii_letters)))
            if current_count_tuple == count_tuple:
                seen.add(i)
                anagram_count += 1
            if anagram_count >= 52:
                return False
    return True