def return_vowels(string: str) -> list:
    vowel_list = []
    for i, c in enumerate(string):
        if i >= 19 and i < 32 and (c > '0') and (c <= '7'):
            vowel_list.append(c)
    return vowel_list