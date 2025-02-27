def palindromes_between_indices(string):
    letters = [char for char in string if char.isalpha()]
    palindromes = set()
    for i in range(3, 7):
        for j in range(len(letters) - i + 1):
            palindrome = ''.join(letters[j:j + i])
            if palindrome.lower() == palindrome[::-1].lower():
                palindromes.add(palindrome)
    return palindromes