def palindrome_of_length_at_least_n(s):
    s = s.lower()
    result = set()

    def is_palindrome(word):
        return word == word[::-1]
    for i in range(len(s) - 12):
        for j in range(i + 13, len(s) + 1):
            substring = s[i:j]
            if is_palindrome(substring) and substring.isalpha():
                result.add(substring)
    return result