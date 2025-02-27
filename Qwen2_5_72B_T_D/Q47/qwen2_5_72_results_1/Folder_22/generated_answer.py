def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = s[100:201]
    result = set()
    for i in range(len(s)):
        for j in range(i + 5, min(i + 11, len(s) + 1)):
            substring = s[i:j]
            if substring.isalpha() and is_palindrome(substring.lower()):
                result.add(substring.lower())
    return result