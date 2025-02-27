def palindromes_of_specific_lengths(s):
    s = s[24:97]
    found_palindromes = set()

    def is_palindrome(substring):
        return substring == substring[::-1]
    for i in range(24, 97 - 10 + 2):
        for j in range(i + 10, min(i + 37, 98)):
            if is_palindrome(s[i:j + 1]):
                found_palindromes.add(s[i:j + 1].lower())
    return found_palindromes