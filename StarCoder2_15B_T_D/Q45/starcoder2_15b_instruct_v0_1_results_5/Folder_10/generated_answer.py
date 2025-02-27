def palindromes_between_indices(string):
    letters = [char for char in string if char.isalpha()]
    palindromes = set()
    for i in range(len(letters) - 2):
        for j in range(i + 2, len(letters) + 1):
            palindrome = ''.join(letters[i:j])
            if len(palindrome) >= 3 and palindrome.lower() == palindrome[::-1].lower():
                palindromes.add(palindrome)
    return palindromes