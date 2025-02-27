def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    valid_range = s[125:284]
    palindromes = set()
    for length in range(109, 127):
        for start in range(len(valid_range) - length + 1):
            sub = valid_range[start:start + length]
            if sub.isalpha() and is_palindrome(sub):
                palindromes.add(sub)
    return palindromes