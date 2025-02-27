def palindromes_between_indices(s):
    chars = [c for c in s[6:10].lower() if c.isalpha()]
    palindromes = set()
    for i in range(len(chars) - 3):
        for j in range(i + 3, len(chars)):
            palindrome = ''.join(chars[i:j + 1])
            palindromes.add(palindrome)
    return palindromes