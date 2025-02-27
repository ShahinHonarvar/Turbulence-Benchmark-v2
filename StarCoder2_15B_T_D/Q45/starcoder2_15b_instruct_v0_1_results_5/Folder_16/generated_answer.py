def palindromes_between_indices(string):
    letters = sorted(string[6:10].lower())
    palindromes = set()

    def generate_palindromes(letters, palindrome, start, end):
        if len(palindrome) == 5:
            palindromes.add(palindrome)
        else:
            for i in range(start, len(letters)):
                generate_palindromes(letters, palindrome + letters[i], i + 1, end - 1)
    generate_palindromes(letters, '', 0, len(letters) - 1)
    return palindromes