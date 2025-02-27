def palindromes_between_indices(string):
    s = string.lower()
    letters = []
    for i in range(len(s)):
        if s[i].isalpha():
            letters.append(s[i])
    palindromes = set()
    for i in range(len(letters) - 4):
        for j in range(i + 4, len(letters)):
            palindrome = ''.join(letters[i:j + 1])
            if len(palindrome) >= 5 and palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes