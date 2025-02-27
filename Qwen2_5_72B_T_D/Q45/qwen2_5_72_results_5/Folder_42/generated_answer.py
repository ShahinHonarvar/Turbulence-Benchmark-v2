def palindromes_between_indices(s):
    substring = s[6:10].lower()
    char_count = {}
    for char in substring:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    palindromes = set()

    def generate_palindrome(half, length):
        if length == 3:
            for char in char_count:
                if char_count[char] > 1:
                    palindromes.add(half + char + half[::-1])
                    return
        elif length == 4:
            for char, count in char_count.items():
                if count > 1:
                    char_count[char] -= 2
                    generate_palindrome(half + char, 3)
                    char_count[char] += 2
    for char, count in char_count.items():
        if count > 1:
            char_count[char] -= 2
            generate_palindrome(char, 4)
            char_count[char] += 2
        if count > 0:
            generate_palindrome('', 3)
    return palindromes