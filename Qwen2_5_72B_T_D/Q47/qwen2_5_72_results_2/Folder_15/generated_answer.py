def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    valid_palindromes = set()
    s_sub = s[:7]
    for length in range(3, 7):
        for start in range(len(s_sub) - length + 1):
            sub = s_sub[start:start + length]
            if sub.isalpha() and is_palindrome(sub):
                valid_palindromes.add(sub.lower())
    return valid_palindromes