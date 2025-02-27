def palindromes_between_indices(s):
    letters = s[4:8]
    letter_count = {}
    for letter in letters:
        if letter.isalpha():
            letter_count[letter.lower()] = letter_count.get(letter.lower(), 0) + 1

    def is_palindrome(word):
        return word == word[::-1]

    def generate_combinations(counts, length):
        if length == 0:
            yield ''
            return
        for letter in sorted(counts.keys()):
            if counts[letter] > 0:
                counts[letter] -= 1
                for combination in generate_combinations(counts, length - 1):
                    yield (letter + combination + letter)
                counts[letter] += 1
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for combination in generate_combinations(letter_count, length):
            if is_palindrome(combination):
                palindromes.add(combination)
    return palindromes