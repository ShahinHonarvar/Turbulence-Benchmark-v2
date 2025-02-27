def is_palindrome(s):
    return s.lower() == s[::-1].lower()

def palindromes_of_specific_lengths(input_string):
    start, end = (31, 74)
    palindromes = set()
    for length in range(23, 40):
        for i in range(start, end - length + 2):
            substring = input_string[i:i + length]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes