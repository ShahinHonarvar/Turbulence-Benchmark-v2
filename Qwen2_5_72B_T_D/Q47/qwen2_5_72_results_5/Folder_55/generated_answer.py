def palindromes_of_specific_lengths(s):

    def is_palindrome(t):
        return t == t[::-1]
    s_sub = s[10:76]
    palindromes = set()
    for i in range(len(s_sub)):
        for j in range(i + 10, i + 21):
            if j <= len(s_sub):
                substr = s_sub[i:j]
                if substr.isalpha() and is_palindrome(substr.lower()):
                    palindromes.add(substr)
    return palindromes