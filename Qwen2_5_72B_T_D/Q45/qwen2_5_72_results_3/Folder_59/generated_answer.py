def palindromes_between_indices(s):
    substring = s[8:10].lower()
    char_freq = {}
    for char in substring:
        if char.isalpha():
            char_freq[char] = char_freq.get(char, 0) + 1
    available_chars = ''.join([char * (count // 2) for char, count in char_freq.items()])
    palindromes = set()

    def generate_palindromes(temp, available_chars):
        if len(temp) == len(available_chars):
            for center in char_freq:
                if char_freq[center] % 2 == 1:
                    palindromes.add(temp + center + temp[::-1])
            if not palindromes:
                palindromes.add(temp + temp[::-1])
        else:
            for i in range(len(available_chars)):
                new_temp = temp + available_chars[i]
                new_available_chars = available_chars[:i] + available_chars[i + 1:]
                generate_palindromes(new_temp, new_available_chars)
    generate_palindromes('', available_chars)
    return {palindrome for palindrome in palindromes if len(palindrome) >= 3}