def palindromes_of_specific_lengths(s):

    def is_palindrome(t):
        return t == t[::-1]
    s = s[23:78]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 13, min(i + 41, len(s) + 1)):
            if is_palindrome(s[i:j].lower()) and s[i:j].isalpha():
                palindromes.add(s[i:j])
    return palindromes