def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    valid_range = s[10:56]
    palindromes = set()
    for length in range(3, 8):
        for start in range(len(valid_range) - length + 1):
            sub = valid_range[start:start + length]
            if sub.isalpha() and is_palindrome(sub):
                palindromes.add(sub.lower())
    return palindromes