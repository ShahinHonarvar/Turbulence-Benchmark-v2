def palindromes_between_indices(s):
    chars = sorted((ch for ch in s if ch.isalpha()))
    palindromes = set()
    for i in range(len(chars) - 2):
        for j in range(i + 1, len(chars) - 1):
            for k in range(j + 1, len(chars)):
                palindrome = chars[i].lower() + chars[j].lower() + chars[k].lower()
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes