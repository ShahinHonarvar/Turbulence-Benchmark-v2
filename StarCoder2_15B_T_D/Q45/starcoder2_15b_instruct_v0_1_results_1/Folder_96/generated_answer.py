def palindromes_between_indices(s):
    chars = [c for c in s[3:9].lower() if c.isalpha()]
    palindromes = set()
    for i in range(len(chars)):
        for j in range(i, len(chars)):
            palindrome = chars[i:j + 1]
            if len(palindrome) >= 6 and palindrome == palindrome[::-1]:
                palindromes.add(''.join(palindrome))
    return palindromes