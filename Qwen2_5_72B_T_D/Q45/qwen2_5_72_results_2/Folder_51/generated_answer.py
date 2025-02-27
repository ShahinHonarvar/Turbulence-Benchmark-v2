def palindromes_between_indices(s):
    substring = s[3:6].lower()
    letter_count = {}
    for char in substring:
        if char.isalpha():
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1
    results = set()
    if len(letter_count) == 1:
        for char in letter_count:
            results.add(char * 3)
    elif len(letter_count) == 2:
        char_list = list(letter_count.keys())
        results.add(char_list[0] + char_list[1] + char_list[0])
        results.add(char_list[1] + char_list[0] + char_list[1])
    return results