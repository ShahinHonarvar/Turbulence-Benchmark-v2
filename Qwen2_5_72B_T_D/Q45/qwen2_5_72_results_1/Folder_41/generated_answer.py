def palindromes_between_indices(s):
    substring = s[2:4].lower()
    char_freq = {}
    for char in substring:
        if char.isalpha():
            char_freq[char] = char_freq.get(char, 0) + 1
    palindromes = set()
    for center in char_freq:
        if char_freq[center] >= 2:
            for side in char_freq:
                if side != center and char_freq[side] > 0:
                    char_freq[side] -= 1
                    char_freq[center] -= 2
                    palindrome = side + center * 2 + side
                    palindromes.add(palindrome)
                    char_freq[side] += 1
                    char_freq[center] += 2
        if char_freq[center] > 0:
            for side1 in char_freq:
                if side1 != center and char_freq[side1] > 0:
                    char_freq[side1] -= 1
                    for side2 in char_freq:
                        if side2 != center and side2 != side1 and (char_freq[side2] > 0):
                            char_freq[side2] -= 1
                            palindrome = side1 + center + side2
                            palindromes.add(palindrome)
                            char_freq[side2] += 1
                    char_freq[side1] += 1
    return palindromes