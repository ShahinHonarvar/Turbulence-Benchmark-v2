def palindrome_of_length_at_least_n(s: str) -> set:

    def is_palindrome(ss: str) -> bool:
        return ss == ss[::-1]
    palindromes = set()
    s_lower = s.lower()
    for i in range(len(s_lower)):
        for length_to_check in range(16, len(s_lower) - i + 1):
            candidate = s_lower[i:i + length_to_check]
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes