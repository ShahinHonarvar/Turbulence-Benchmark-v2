def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s[45:99]
    palindromes = set()
    for length in range(40, 48):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length].lower()
            if sub.isalpha() and is_palindrome(sub):
                palindromes.add(sub)
    return palindromes