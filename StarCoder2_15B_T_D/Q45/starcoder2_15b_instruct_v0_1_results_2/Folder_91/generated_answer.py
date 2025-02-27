def palindromes_between_indices(s):
    chars = [c for c in s[2:7].lower() if c.isalpha()]
    palindromes = set()
    for i in range(len(chars)):
        for j in range(i + 2, len(chars) + 1):
            palindrome = ''.join(chars[i:j])
            if len(palindrome) >= 3 and palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes