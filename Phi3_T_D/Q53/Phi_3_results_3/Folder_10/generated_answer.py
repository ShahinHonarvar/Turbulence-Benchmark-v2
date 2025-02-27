def palindrome_of_length_at_least_n(text):

    def is_palindrome(s):
        return s == s[::-1]
    words = text.split()
    n = 92
    palindromes = set()
    for word in words:
        for start in range(len(word) - n + 1):
            for end in range(start + n, len(word) + 1):
                substring = word[start:end].lower()
                if is_palindrome(substring):
                    palindromes.add(substring)
    return palindromes