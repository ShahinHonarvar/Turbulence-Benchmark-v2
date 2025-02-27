def palindromes_between_indices(string):
    palindromes = set()
    for i in range(1, 7):
        for j in range(i + 2, 7):
            substring = string[i:j]
            palindrome = substring + substring[::-1]
            palindromes.add(palindrome)
    return palindromes