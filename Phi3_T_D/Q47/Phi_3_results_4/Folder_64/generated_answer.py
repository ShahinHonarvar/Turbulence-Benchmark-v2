def palindromes_of_specific_lengths(s):
    sub = s[:8].lower()
    palindromes_set = set()

    def is_palindrome(chars):
        return chars == chars[::-1]
    for len_ in range(4, 6):
        for i in range(len(sub) - len_ + 1):
            substring = sub[i:i + len_]
            if all((c.isalpha() for c in substring)) and is_palindrome(substring):
                palindromes_set.add(substring)
    return palindromes_set