def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = s[23:78].lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 13, i + 41):
            if j <= len(s):
                substring = s[i:j]
                if substring.isalpha() and is_palindrome(substring):
                    result.add(substring)
    return result