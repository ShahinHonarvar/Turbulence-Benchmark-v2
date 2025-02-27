def palindromes_of_specific_lengths(input_string):
    input_string_range = input_string[200:301]
    palindromes = set()

    def is_valid_palindrome(s):
        s = ''.join((c for c in s if c.isalpha())).lower()
        return s == s[::-1] and 10 <= len(s) <= 50
    for length in range(10, 51):
        for i in range(200, 301 - length + 1):
            if is_valid_palindrome(input_string_range[i:i + length]):
                palindromes.add(input_string_range[i:i + length])
    return palindromes