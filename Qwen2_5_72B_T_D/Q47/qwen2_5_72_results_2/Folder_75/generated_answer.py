def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = s[31:75]
    palindromes = set()
    for length in range(23, 40):
        for start in range(len(s) - length + 1):
            substr = s[start:start + length]
            if substr.isalpha() and is_palindrome(substr.lower()):
                palindromes.add(substr)
    return palindromes