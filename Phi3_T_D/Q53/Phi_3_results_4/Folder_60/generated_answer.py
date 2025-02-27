def palindrome_of_length_at_least_n(s: str, n: int=80) -> set:
    s_upper = s.upper()
    palindromes = set()
    for i in range(len(s_upper)):
        for j in range(i + n, len(s_upper)):
            substr = s_upper[i:j + 1]
            if substr == substr[::-1] and all((c.isalpha() for c in substr)):
                palindromes.add(substr)
    return palindromes