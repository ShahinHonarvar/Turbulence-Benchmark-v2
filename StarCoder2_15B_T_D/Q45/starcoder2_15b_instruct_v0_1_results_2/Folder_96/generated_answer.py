def palindromes_between_indices(s):
    chars_in_range = [c.lower() for c in s[3:9] if c.isalpha()]
    palindromes = set()
    for i in range(len(chars_in_range)):
        for j in range(i + 6 - 1, len(chars_in_range)):
            palindrome = ''.join(chars_in_range[i:j + 1])
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes