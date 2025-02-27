def palindromes_of_specific_lengths(s):

    def is_palindrome(x):
        return x.lower() == x[::-1].lower()
    s = s[44:100]
    result = set()
    for i in range(len(s)):
        for j in range(i + 13, i + 43):
            if j <= len(s) and s[i:j].isalpha() and is_palindrome(s[i:j]):
                result.add(s[i:j].lower())
    return result