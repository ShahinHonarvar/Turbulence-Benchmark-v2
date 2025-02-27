def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr.lower() == substr[::-1].lower() and substr.isalpha()
    length = 35
    palindromes = set()
    while length <= 41:
        for i in range(32, 79 - length + 2):
            if is_palindrome(s[i:i + length]):
                palindromes.add(s[i:i + length].lower())
        length += 1
    return palindromes