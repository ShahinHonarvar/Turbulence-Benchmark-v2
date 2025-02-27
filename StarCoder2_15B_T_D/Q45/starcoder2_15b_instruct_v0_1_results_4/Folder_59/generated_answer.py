def palindromes_between_indices(s: str) -> set:
    s = s.lower()
    palindromes = set()
    for i in range(8, len(s) - 1):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                palindrome = s[i] + s[i + 1:j] + s[i]
                if len(palindrome) >= 3:
                    palindromes.add(palindrome)
    return palindromes