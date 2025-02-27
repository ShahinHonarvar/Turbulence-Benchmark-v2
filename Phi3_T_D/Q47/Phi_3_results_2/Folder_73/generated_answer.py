def palindromes_of_specific_lengths(s):
    len_s = len(s)
    start = 21
    end = min(len_s, 62)
    valid_palindromes = set()

    def is_valid_palindrome(substring):
        return substring.lower() == substring[::-1].lower() and substring.isalpha()
    for length in range(22, 34):
        for i in range(start, end - length + 1):
            substring = s[i:i + length]
            if is_valid_palindrome(substring):
                valid_palindromes.add(substring.lower())
    return valid_palindromes