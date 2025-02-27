def palindromes_of_specific_lengths(s):

    def is_palindrome(w):
        return w == w[::-1]
    s = s[1:300]
    palindromes = set()
    for length in range(3, 11):
        for i in range(len(s) - length + 1):
            substr = s[i:i + length]
            if substr.isalpha() and is_palindrome(substr.lower()):
                palindromes.add(substr)
    return palindromes