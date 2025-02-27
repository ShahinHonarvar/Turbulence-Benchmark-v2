import itertools

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(text):
    letters_from_index_2_to_8 = text[2:10].lower()
    letter_counts = {}
    for letter in letters_from_index_2_to_8:
        if letter.isalpha():
            letter_counts[letter] = letter_counts.get(letter, 0) + 1
    palindromes = set()
    for length in range(6, len(letters_from_index_2_to_8) + 1, 2):
        for combo in itertools.permutations(letters_from_index_2_to_8, length):
            if combo[:length // 2] == combo[length // 2:][::-1]:
                counting = {letter: combo.count(letter) for letter in letter_counts}
                if all((count in range(letter_counts[letter], letter_counts[letter] + 1) for letter in counting)):
                    palindromes.add(''.join(combo))
    return palindromes