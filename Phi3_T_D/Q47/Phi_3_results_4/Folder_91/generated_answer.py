def is_palindrome(s: str) -> bool:
    return s.lower() == s[::-1].lower()

def palindromes_of_specific_lengths(string: str) -> set:
    substring_range = string[:11]
    palindromes = set()
    for length in range(3, 6):
        for i in range(len(substring_range) - length + 1):
            possible_palindrome = substring_range[i:i + length]
            if is_palindrome(possible_palindrome) and possible_palindrome.isalpha():
                palindromes.add(possible_palindrome)
    return palindromes