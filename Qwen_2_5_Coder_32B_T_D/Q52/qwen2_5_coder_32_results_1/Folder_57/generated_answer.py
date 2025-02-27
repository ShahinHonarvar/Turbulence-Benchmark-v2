def palindrome_of_length_n(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = s.lower()
    result = set()
    for i in range(len(s) - 91):
        substring = s[i:i + 92]
        if substring.isalpha() and is_palindrome(substring):
            result.add(substring)
    return result