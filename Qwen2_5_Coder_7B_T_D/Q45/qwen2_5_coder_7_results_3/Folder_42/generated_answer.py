def palindromes_between_indices(s):
    letters = s[6:10]
    letters = ''.join(filter(str.isalpha, letters)).lower()
    letters = ''.join(sorted(set(letters)))
    result = set()
    for i in range(len(letters)):
        for j in range(i + 2, len(letters) + 1):
            palindrome = letters[i:j]
            if palindrome == palindrome[::-1]:
                result.add(palindrome)
    return result