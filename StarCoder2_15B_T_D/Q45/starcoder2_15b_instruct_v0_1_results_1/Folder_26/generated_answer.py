def palindromes_between_indices(string):
    letters = sorted(string[4:7].lower())
    palindromes = set()

    def generate_palindromes(letters, current, length):
        if len(current) == length:
            palindromes.add(''.join(current))
        else:
            for i, letter in enumerate(letters):
                generate_palindromes(letters[i + 1:], current + [letter], length)
    for length in range(3, len(letters) + 1):
        generate_palindromes(letters, [], length)
    return palindromes