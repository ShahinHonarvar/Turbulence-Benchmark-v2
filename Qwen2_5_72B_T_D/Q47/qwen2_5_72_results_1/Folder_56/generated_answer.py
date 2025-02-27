def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    valid_range = s[1:10]
    palindromes = set()
    for length in range(3, 8):
        for start in range(len(valid_range) - length + 1):
            substr = valid_range[start:start + length]
            if substr.isalpha() and is_palindrome(substr):
                palindromes.add(substr)
    return palindromes