def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    s = s[32:72]
    palindromes = set()
    for length in range(21, 33):
        for start in range(len(s) - length + 1):
            sub = s[start:start + length]
            if sub.isalpha() and is_palindrome(sub):
                palindromes.add(sub)
    return palindromes