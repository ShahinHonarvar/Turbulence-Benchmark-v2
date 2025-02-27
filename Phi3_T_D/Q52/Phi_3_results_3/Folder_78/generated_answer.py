def palindrome_of_length_n(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    result = set()
    length = 48
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if all((c.isalpha() for c in substring)) and is_palindrome(substring):
            result.add(substring)
    return result