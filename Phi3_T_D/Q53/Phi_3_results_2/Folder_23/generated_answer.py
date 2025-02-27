def palindrome_of_length_at_least_n(s):
    s = s.lower()
    result = set()

    def is_palindrome(word):
        return word == word[::-1]
    for i in range(len(s)):
        for length in range(19, len(s) - i + 1):
            word = s[i:i + length]
            if is_palindrome(word):
                result.add(word)
    return result