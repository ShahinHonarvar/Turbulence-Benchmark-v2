def palindromes_between_indices(string):
    chars = [c for c in string[1:6].lower() if c.isalpha()]
    palindromes = set()
    for i in range(len(chars)):
        for j in range(i + 6, len(chars) + 1):
            palindrome = ''.join(chars[i:j])
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes