def palindrome_of_length_at_least_n(s):

    def is_palindrome(word):
        return word == word[::-1]

    def find_palindromes(s, n, i, word, direction):
        if n < 97:
            return
        if i < 0 or i >= len(s):
            if is_palindrome(word) and (not direction):
                return {word}
            return set()
        return (find_palindromes(s, n - 1, i - 1, word + s[i].lower(), direction) | find_palindromes(s, n - 1, i + 1, word + s[i].lower(), direction) if direction else None) | (direction and find_palindromes(s, n - 1, i - 1, word, True))
    s = s.lower()
    result = set()
    for i in range(len(s)):
        if s[i].isalpha():
            result |= find_palindromes(s, len(s) - i, i, '', True)
    return result