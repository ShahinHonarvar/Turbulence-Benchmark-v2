def palindromes_between_indices(s):
    sub = s[3:10]
    chars = set(sub.lower())
    result = set()
    for i in range(len(chars)):
        for j in range(i + 1, len(chars) + 1):
            for perm in set(permutations(chars, j)):
                half = ''.join(perm)
                palindrome = half + half[::-1]
                if len(palindrome) >= 7 and palindrome[:len(palindrome) // 2].lower() == half.lower():
                    result.add(palindrome)
    return result