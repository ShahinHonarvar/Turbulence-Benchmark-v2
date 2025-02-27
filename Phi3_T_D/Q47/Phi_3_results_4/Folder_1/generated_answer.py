def is_palindrome(s):
    return s.lower() == s[::-1].lower()

def filter_palindromes_in_range_with_specific_lengths(text, start, end, min_length, max_length):
    eligible_palindromes = set()
    for idx in range(start, end + 1):
        for length in range(min_length, max_length + 1):
            substring = text[idx:idx + length]
            if is_palindrome(substring) and substring.isalpha():
                eligible_palindromes.add(substring)
    return eligible_palindromes

def palindromes_of_specific_lengths(text):
    return filter_palindromes_in_range_with_specific_lengths(text, 15, 89, 40, 72)