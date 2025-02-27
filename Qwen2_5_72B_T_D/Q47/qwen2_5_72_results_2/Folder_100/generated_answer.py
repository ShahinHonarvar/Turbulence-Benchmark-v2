def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    valid_range = s[29:97]
    palindromes = set()
    for length in range(12, 19):
        for start in range(len(valid_range) - length + 1):
            sub = valid_range[start:start + length]
            if is_palindrome(sub) and sub.isalpha():
                palindromes.add(sub)
    return palindromes