def palindrome_of_length_at_least_n(s):

    def is_palindrome(word):
        return word == word[::-1] and all(('a' <= char.lower() <= 'z' for char in word))
    length = len(s)
    palindromes = set()
    for start in range(length):
        for end in range(start + 34, length + 1):
            substring = s[start:end]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes