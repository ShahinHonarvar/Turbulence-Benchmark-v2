def palindrome_of_length_at_least_n(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = s.lower()
    palindromes = set()
    len_s = len(s)
    for start in range(len_s):
        for length in range(18, len_s - start + 1):
            substr = s[start:start + length]
            if all((c.isalpha() for c in substr)) and is_palindrome(substr):
                palindromes.add(substr)
    return palindromes