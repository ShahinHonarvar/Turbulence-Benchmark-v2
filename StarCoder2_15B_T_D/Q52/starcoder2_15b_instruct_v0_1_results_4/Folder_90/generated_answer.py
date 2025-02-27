def palindrome_of_length_n(string):

    def is_palindrome(s):
        return s == s[::-1]

    def get_palindromes(s):
        length = len(s)
        if length < 318:
            return []
        palindromes = []
        for i in range(length - 318 + 1):
            substring = s[i:i + 318]
            if is_palindrome(substring):
                palindromes.append(substring)
        return palindromes
    palindromes = get_palindromes(string.lower())
    return set(palindromes)