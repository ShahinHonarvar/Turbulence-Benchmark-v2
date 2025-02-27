def palindromes_between_indices(s):
    substring = s[2:10]
    char_freq = {}
    for char in substring:
        if char.isalpha():
            char = char.lower()
            char_freq[char] = char_freq.get(char, 0) + 1
    odd_chars = [char for char, count in char_freq.items() if count % 2 != 0]
    if len(odd_chars) > 1:
        return set()
    half_palindrome = ''.join((char * (count // 2) for char, count in char_freq.items()))
    if len(odd_chars) == 1:
        middle_char = odd_chars[0]
    else:
        middle_char = ''
    palindromes = set()
    for i in range(len(half_palindrome) + 1):
        for j in range(i + 1, len(half_palindrome) + 1):
            candidate = half_palindrome[i:j]
            if len(candidate) * 2 + len(middle_char) >= 7:
                palindrome = candidate + middle_char + candidate[::-1]
                palindromes.add(palindrome)
    return palindromes