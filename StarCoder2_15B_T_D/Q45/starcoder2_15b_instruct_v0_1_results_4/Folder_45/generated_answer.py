def palindromes_between_indices(string):
    chars = [char for char in string.lower() if char.isalpha()]
    palindromes = set()
    for i in range(5, min(9, len(chars)) + 1):
        for j in range(len(chars) - i + 1):
            palindrome = chars[j:j + i]
            if palindrome == palindrome[::-1]:
                palindromes.add(''.join(palindrome))
    return palindromes