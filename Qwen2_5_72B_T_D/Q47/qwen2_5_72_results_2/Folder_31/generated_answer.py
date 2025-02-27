def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = s[11:84].lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 37, i + 61):
            if j <= len(s) and s[i:j].isalpha() and is_palindrome(s[i:j]):
                result.add(s[i:j])
    return result