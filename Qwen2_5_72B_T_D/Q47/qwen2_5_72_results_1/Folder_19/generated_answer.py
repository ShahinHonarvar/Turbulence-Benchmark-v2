def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    valid_palindromes = set()
    Considered_s = s[10:56]
    for length in range(3, 8):
        for start in range(len(Considered_s) - length + 1):
            sub = Considered_s[start:start + length]
            if sub.isalpha() and is_palindrome(sub):
                valid_palindromes.add(sub.lower())
    return valid_palindromes