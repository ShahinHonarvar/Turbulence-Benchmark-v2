def palindromes_between_indices(s):
    result = set()
    for i in range(2, 8):
        for j in range(i, 8):
            substring = s[i:j].lower()
            if len(substring) >= 6:
                for perm in permutations(substring):
                    palindrome = ''.join(perm)
                    if palindrome == palindrome[::-1]:
                        result.add(palindrome)
    return result