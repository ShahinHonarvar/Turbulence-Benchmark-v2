def palindrome_of_length_at_least_n(s):

    def is_palindrome(word):
        return word == word[::-1]
    result = set()
    length = len(s)
    s = s.lower()
    for i in range(length):
        for j in range(i + 33, length + 1):
            substr = s[i:j]
            if substr.isalpha() and is_palindrome(substr):
                result.add(substr)
    return result