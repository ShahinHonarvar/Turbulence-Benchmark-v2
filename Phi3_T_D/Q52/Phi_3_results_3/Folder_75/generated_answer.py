def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()

    def is_palindrome(substring):
        return substring == substring[::-1]
    for i in range(len(s) - 79):
        substring = s[i:i + 80]
        if is_palindrome(substring):
            palindromes.add(substring)
    return palindromes