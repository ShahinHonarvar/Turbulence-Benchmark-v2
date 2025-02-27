def palindromes_between_indices(s):
    substring = s[0:7]
    letter_counts = {}
    for letter in substring:
        if letter.isalpha():
            letter = letter.lower()
            if letter in letter_counts:
                letter_counts[letter] += 1
            else:
                letter_counts[letter] = 1
    half_palindrome = ''
    middle = ''
    for letter, count in letter_counts.items():
        half_palindrome += letter * (count // 2)
        if count % 2 != 0 and middle == '':
            middle = letter
    palindromes = set()
    if len(half_palindrome) >= 2:
        for i in range(1, len(half_palindrome) + 1):
            for perm in set(itertools.permutations(half_palindrome, i)):
                palindrome = ''.join(perm) + middle + ''.join(reversed(perm))
                if len(palindrome) >= 5:
                    palindromes.add(palindrome)
    return palindromes