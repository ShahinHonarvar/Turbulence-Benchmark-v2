def palindromes_of_specific_lengths(s):

    def is_palindrome(substring):
        return substring == substring[::-1]
    start_idx, end_idx = (127, min(len(s), 288))
    palindromes = set()
    for length in range(119, 142):
        for i in range(start_idx, end_idx - length + 1):
            substring = s[i:i + length]
            if substring.isalpha() and is_palindrome(substring):
                palindromes.add(substring.lower())
    return palindromes