def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    s = s[36:93]
    palindromes = set()
    for length in range(10, 36):
        for start in range(len(s) - length + 1):
            sub = s[start:start + length]
            if sub.isalpha() and is_palindrome(sub):
                palindromes.add(sub.lower())
    return palindromes