def palindrome_of_length_at_least_n(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = s.lower()
    palindromes_set = set()
    for length in range(68, len(s) + 1):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if all((c.isalpha() for c in substring)) and is_palindrome(substring):
                palindromes_set.add(substring)
    return palindromes_set