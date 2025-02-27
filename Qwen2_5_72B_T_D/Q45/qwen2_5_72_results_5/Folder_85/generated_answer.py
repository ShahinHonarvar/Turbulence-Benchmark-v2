def palindromes_between_indices(s):
    substring = s[2:9]
    letter_count = {}
    for letter in substring:
        if letter.isalpha():
            letter = letter.lower()
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    odd_chars = [char for char, count in letter_count.items() if count % 2 != 0]
    if len(odd_chars) > 1:
        return set()
    else:
        half_palindrome = ''.join([char * (count // 2) for char, count in sorted(letter_count.items())])
        palindrome = half_palindrome
        if odd_chars:
            palindrome += odd_chars[0]
        palindrome += half_palindrome[::-1]
        all_palindromes = set()
        if len(palindrome) >= 7:
            for i in range(len(palindrome) - 6):
                all_palindromes.add(palindrome[i:i + 7])
        return all_palindromes