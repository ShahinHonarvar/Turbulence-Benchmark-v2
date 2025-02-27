def palindrome_of_length_n(s):
    s = s.lower()

    def is_palindrome(substring):
        return substring == substring[::-1]
    palindromes = set()
    s_length = len(s)
    for i in range(s_length - 20):
        substring = s[i:i + 21]
        if is_palindrome(substring):
            palindromes.add(substring)
    return palindromes