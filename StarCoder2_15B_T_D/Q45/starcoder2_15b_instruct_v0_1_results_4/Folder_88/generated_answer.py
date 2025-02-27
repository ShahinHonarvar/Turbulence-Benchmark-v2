def palindromes_between_indices(string):
    sub_string = string[3:8]
    letters = [c for c in sub_string if c.isalpha()]
    palindromes = set()
    for i in range(len(letters) - 5):
        for j in range(i + 6, len(letters)):
            palindrome = ''.join(letters[i:j])
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes