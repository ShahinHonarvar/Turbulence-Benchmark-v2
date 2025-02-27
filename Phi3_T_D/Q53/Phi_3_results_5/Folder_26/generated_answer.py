def is_palindrome(s):
    return s == s[::-1]

def palindrome_of_length_at_least_n(input_string):
    input_string = input_string.lower()
    all_palindromes = set()
    length = len(input_string)
    for palindrome_length in range(32, length + 1):
        for start_index in range(length - palindrome_length + 1):
            candidate = input_string[start_index:start_index + palindrome_length]
            if is_palindrome(candidate):
                all_palindromes.add(candidate)
    all_palindromes = {p for p in all_palindromes if p.isalpha()}
    return all_palindromes