def palindrome_of_length_at_least_n(s):

    def is_palindrome(word):
        return word == word[::-1]

    def valid_characters(word):
        return all(('a' <= c <= 'z' for c in word))
    length = 68
    palindromes = set()
    s_lower = s.lower()
    for i in range(len(s_lower)):
        for j in range(i + length, len(s_lower) + 1):
            substring = s_lower[i:j]
            if is_palindrome(substring) and all((valid_characters(c) for c in substring)):
                palindromes.add(substring)
    return palindromes