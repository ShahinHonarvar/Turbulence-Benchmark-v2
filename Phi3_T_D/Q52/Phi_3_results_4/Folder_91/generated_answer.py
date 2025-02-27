def palindrome_of_length_n(s):
    if len(s) < 7:
        return set()

    def is_palindrome(substring):
        return substring == substring[::-1]
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - 6):
        substring = s[i:i + 7]
        if is_palindrome(substring):
            palindromes.add(substring)
    return palindromes