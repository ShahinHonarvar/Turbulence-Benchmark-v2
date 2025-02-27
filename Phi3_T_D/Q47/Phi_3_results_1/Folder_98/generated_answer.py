def is_palindrome(s: str) -> bool:
    return s == s[::-1]

def palindromes_of_specific_lengths(input_string):
    palindromes_set = set()
    upper_limit = min(len(input_string), 20)
    for i in range(upper_limit):
        for length in range(5, 80 + 1):
            if i + length > upper_limit:
                break
            substring = input_string[i:i + length]
            cleaned_substring = ''.join(filter(str.isalpha, substring)).lower()
            if 5 <= len(cleaned_substring) <= 80 and is_palindrome(cleaned_substring):
                palindromes_set.add(cleaned_substring)
    return palindromes_set