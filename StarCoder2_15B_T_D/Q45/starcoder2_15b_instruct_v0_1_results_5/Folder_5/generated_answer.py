def palindromes_between_indices(string):
    letters = [char for char in string if char.isalpha()]
    palindromes = set()
    for i in range(4, len(letters) - 3):
        for j in range(i + 2, len(letters)):
            palindrome = ''.join(letters[i:j + 1]).lower()
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes