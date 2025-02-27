def palindromes_of_specific_lengths(s):

    def is_palindrome(substring):
        return substring == substring[::-1]
    s = s[:51]
    palindromes = set()
    for length in range(50, 101):
        for i in range(50 - length + 1):
            if is_palindrome(s[i:i + length]) and s[i:i + length].isalpha():
                palindromes.add(s[i:i + length])
    return palindromes