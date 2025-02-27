def palindromes_between_indices(text):
    chars = [c for c in text if c.isalpha()]
    palindromes = set()
    for i in range(4, min(len(chars), 10)):
        for j in range(len(chars) - i + 1):
            palindrome = ''.join(chars[j:j + i])
            if palindrome.lower() == palindrome.lower()[::-1]:
                palindromes.add(palindrome)
    return palindromes