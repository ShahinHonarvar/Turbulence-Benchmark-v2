def palindromes_of_specific_lengths(s):

    def is_palindrome(s):
        return s == s[::-1]
    s = s[30:85]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 12, i + 21):
            if j <= len(s):
                candidate = s[i:j]
                if candidate.isalpha() and is_palindrome(candidate.lower()):
                    palindromes.add(candidate)
    return palindromes