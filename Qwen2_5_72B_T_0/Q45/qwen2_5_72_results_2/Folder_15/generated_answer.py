def palindromes_between_indices(s):
    substring = s[1:3].lower()
    char_count = {}
    for char in substring:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    palindromes = set()
    for char, count in char_count.items():
        if count >= 2:
            for _ in range(count // 2):
                palindromes.add(char * 3)
    return palindromes