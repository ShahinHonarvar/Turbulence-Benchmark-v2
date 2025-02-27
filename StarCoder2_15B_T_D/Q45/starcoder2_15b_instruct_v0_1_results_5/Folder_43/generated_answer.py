def palindromes_between_indices(string):
    letters = [char for char in string if char.isalpha()]
    palindromes = set()
    for i in range(2, len(letters) - 1):
        for j in range(i + 1, len(letters)):
            palindrome = letters[i:j + 1][::-1]
            if len(palindrome) >= 4 and palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes