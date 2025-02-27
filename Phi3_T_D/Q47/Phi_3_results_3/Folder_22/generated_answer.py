def palindromes_of_specific_lengths(string):

    def is_palindrome(s: str) -> bool:
        return s == s[::-1]
    string = string[99:201]
    palindromes = set()
    for length in range(5, 11):
        for i in range(100 - length + 1):
            candidate = string[i:i + length]
            if is_palindrome(candidate) and candidate.isalpha():
                palindromes.add(candidate.lower())
    return palindromes