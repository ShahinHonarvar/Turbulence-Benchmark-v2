def palindromes_of_specific_lengths(s):

    def is_palindrome(w):
        return w == w[::-1]
    s = s[:8]
    s = ''.join(filter(str.isalpha, s))
    s = s.lower()
    palindromes = set()
    for length in range(4, 6):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes