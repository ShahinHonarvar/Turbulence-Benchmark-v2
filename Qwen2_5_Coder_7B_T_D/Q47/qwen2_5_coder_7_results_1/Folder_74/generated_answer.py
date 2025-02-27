def palindromes_of_specific_lengths(s: str) -> set:
    substr = s[30:85].lower()
    palindromes = set()
    for i in range(len(substr)):
        for j in range(i + 12, min(len(substr), i + 21)):
            substring = substr[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes