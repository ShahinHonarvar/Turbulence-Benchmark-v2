def palindromes_of_specific_lengths(s):

    def is_palindrome(x):
        return x.lower() == x[::-1].lower()

    def has_only_letters(x):
        return all((c.isalpha() for c in x))
    substr = s[21:63]
    valid_palindromes = set()
    for length in range(22, 34):
        for start in range(len(substr) - length + 1):
            candidate = substr[start:start + length]
            if is_palindrome(candidate) and has_only_letters(candidate):
                valid_palindromes.add(candidate)
    return valid_palindromes