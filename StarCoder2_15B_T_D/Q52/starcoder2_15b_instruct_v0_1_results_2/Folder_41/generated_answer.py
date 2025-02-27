def is_palindrome(string: str) -> bool:
    return string == string[::-1]

def palindrome_of_length_n(string: str, n: int) -> set:
    cleaned_string = ''.join((c for c in string.lower() if c.isalpha()))
    palindromes = set()
    for i in range(len(cleaned_string) - n + 1):
        substring = cleaned_string[i:i + n]
        if is_palindrome(substring):
            palindromes.add(substring)
    return palindromes