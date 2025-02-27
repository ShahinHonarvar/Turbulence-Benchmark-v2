def palindromes_of_specific_lengths(s):
    start, end = (43, 95)
    s = s[start:end + 1].lower()
    palindromes = set()

    def is_palindrome(sub):
        return sub == sub[::-1]
    for length in range(18, 48):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if sub.isalpha() and is_palindrome(sub):
                palindromes.add(sub)
    return palindromes