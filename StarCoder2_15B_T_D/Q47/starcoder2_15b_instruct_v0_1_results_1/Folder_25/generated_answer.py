def palindromes_of_specific_lengths(string):
    substring = string[26:85]

    def is_palindrome(string):
        return string == string[::-1]

    def is_length_valid(string):
        return len(string) >= 30 and len(string) <= 46

    def is_alphabetic(string):
        return string.isalpha()
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 1, len(substring)):
            substring = string[i:j]
            if is_palindrome(substring) and is_length_valid(substring) and is_alphabetic(substring):
                palindromes.add(substring)
    return palindromes