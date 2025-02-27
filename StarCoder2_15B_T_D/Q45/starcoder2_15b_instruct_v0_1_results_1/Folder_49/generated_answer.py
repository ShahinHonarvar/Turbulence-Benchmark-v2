def palindromes_between_indices(string):
    letters = [c for c in string if c.isalpha()]
    palindromes = set()
    for i in range(5, 8):
        for j in range(i + 1, 8):
            substring = letters[i:j]
            reversed_substring = substring[::-1]
            palindrome = substring + reversed_substring
            palindromes.add(''.join(palindrome))
    return palindromes