def palindrome_of_length_at_least_n(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    result = set()
    s = ''.join(filter(str.isalpha, s))
    for i in range(len(s)):
        for j in range(i + 118, len(s)):
            candidate = s[i:j + 1]
            if is_palindrome(candidate):
                result.add(candidate)
    return result