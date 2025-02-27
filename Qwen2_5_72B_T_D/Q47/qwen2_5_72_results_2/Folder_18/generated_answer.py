def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = s[11:84]
    result = set()
    for i in range(len(s)):
        for j in range(i + 13, min(i + 67, len(s) + 1)):
            substring = s[i:j]
            if substring.isalpha() and is_palindrome(substring.lower()):
                result.add(substring)
    return result