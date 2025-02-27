def palindromes_of_specific_lengths(s):

    def is_palindrome(x):
        return x == x[::-1]
    s = s[11:88]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 4, min(i + 6, len(s) + 1)):
            substr = s[i:j]
            if substr.isalpha() and is_palindrome(substr.lower()):
                palindromes.add(substr)
    return palindromes