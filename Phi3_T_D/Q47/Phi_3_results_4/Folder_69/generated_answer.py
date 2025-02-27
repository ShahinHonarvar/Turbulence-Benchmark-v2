def is_palindrome(s):
    return s == s[::-1]

def palindromes_of_specific_lengths(text):
    candidate_str = text[11:97]
    return {candidate_str[i:i + length] for length in range(45, 53) for i in range(len(candidate_str) - length + 1) if is_palindrome(candidate_str[i:i + length]) and candidate_str[i:i + length].isalpha()}