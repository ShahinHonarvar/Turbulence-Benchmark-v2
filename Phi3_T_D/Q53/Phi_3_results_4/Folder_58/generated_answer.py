def palindrome_of_length_at_least_n(input_string):
    n = 147
    lowered = input_string.lower()
    valid_chars = set('abcdefghijklmnopqrstuvwxyz')
    found_palindromes = set()
    for i in range(len(lowered)):
        for length in range(n, len(lowered) - i + 1):
            potential_palindrome = lowered[i:i + length]
            if all((char in valid_chars for char in potential_palindrome)) and potential_palindrome == potential_palindrome[::-1]:
                found_palindromes.add(potential_palindrome)
    return found_palindromes