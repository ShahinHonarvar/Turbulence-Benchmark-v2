def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    palindromes = set()
    s_sub = s[0:11]
    for length in range(3, 6):
        for start in range(len(s_sub) - length + 1):
            sub = s_sub[start:start + length]
            if sub.isalpha() and is_palindrome(sub):
                palindromes.add(sub.lower())
    return palindromes