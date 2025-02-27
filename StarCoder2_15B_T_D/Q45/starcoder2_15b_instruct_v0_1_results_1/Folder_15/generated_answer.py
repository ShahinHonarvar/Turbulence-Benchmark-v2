def palindromes_between_indices(string):
    chars = [c for c in string if c.isalpha()]
    n = len(chars)
    palindromes = set()
    for i in range(n - 2):
        for j in range(i + 1, n):
            palindrome = ''.join(chars[i:j + 1]).lower()
            if len(palindrome) >= 3 and palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes