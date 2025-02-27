def palindromes_of_specific_lengths(s):
    s = ''.join((c for c in s[:101] if c.isalpha())).lower()

    def is_palindrome(sub):
        return sub == sub[::-1] and 2 < len(sub) <= 15
    palindromes = set()
    for length in range(3, 16):
        for i in range(len(s) - length + 1):
            if is_palindrome(s[i:i + length]):
                palindromes.add(s[i:i + length])
    return palindromes