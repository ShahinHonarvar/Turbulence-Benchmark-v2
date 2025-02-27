def palindromes_between_indices(text):
    letters = [c for c in text if c.isalpha()]
    palindromes = set()
    for i in range(1, len(letters) - 5):
        for j in range(i + 6, len(letters) + 1):
            substring = letters[i:j]
            reversed_substring = substring[::-1]
            palindrome = substring + reversed_substring
            palindromes.add(''.join(palindrome).lower())
    return palindromes