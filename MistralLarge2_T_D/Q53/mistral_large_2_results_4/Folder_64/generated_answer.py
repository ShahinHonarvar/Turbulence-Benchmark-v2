def palindrome_of_length_at_least_n(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = ''.join((c for c in s if c.isalpha())).lower()
    palindromes = set()
    for length in range(9, len(s) + 1):
        for i in range(len(s) - length + 1):
            candidate = s[i:i + length]
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes