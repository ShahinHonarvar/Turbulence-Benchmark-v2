def is_palindrome(s):
    return s == s[::-1]

def palindromes_of_specific_lengths(input_string):
    input_string = input_string[45:99].lower()
    palindromes = set()
    for length in range(40, 48):
        for start_pos in range(len(input_string) - length + 1):
            substring = input_string[start_pos:start_pos + length]
            if substring.isalpha() and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes