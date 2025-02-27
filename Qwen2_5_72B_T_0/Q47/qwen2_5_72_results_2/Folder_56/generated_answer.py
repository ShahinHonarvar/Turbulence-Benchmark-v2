def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    valid_palindromes = set()
    substring = s[1:10]
    for length in range(3, 8):
        for start in range(len(substring) - length + 1):
            sub = substring[start:start + length]
            if sub.isalpha() and is_palindrome(sub):
                valid_palindromes.add(sub.lower())
    return valid_palindromes