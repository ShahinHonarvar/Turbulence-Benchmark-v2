import itertools

def palindromes_between_indices(text):
    letters = [c.lower() for c in text[5:10]]
    letter_counts = {}
    for letter in letters:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1

    def build_palindrome(chars, counts):
        end = [k * (v // 2) for k, v in counts.items()]
        middle = [k for k, v in counts.items() if v % 2]
        start = end.copy()
        return ''.join(start) + ''.join(middle) + ''.join(start[::-1])
    letters_combinations = set()
    for i in range(6, 10):
        for combo in itertools.combinations_with_replacement(letter_counts.keys(), i):
            counts = {char: combo.count(char) for char in combo}
            if all((val % 2 == 0 for val in counts.values())):
                letters_combinations.add(build_palindrome(combo, counts))
    return letters_combinations