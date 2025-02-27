def palindromes_between_indices(string):
    chars = [char for char in string.lower() if char.isalpha()]
    palindromes = set()
    for i in range(2, 10):
        for j in range(i + 1, 10):
            for k in range(j + 1, 10):
                for l in range(k + 1, 10):
                    palindrome = chars[i:j] + chars[k:l][::-1]
                    if len(palindrome) >= 4 and palindrome == palindrome[::-1]:
                        palindromes.add(palindrome)
    return palindromes