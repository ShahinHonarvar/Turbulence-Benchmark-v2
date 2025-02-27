from re import finditer

def palindromes_of_specific_lengths(input_str):
    pals = set()
    substring = input_str[10:76]
    for s in finditer('[a-zA-Z]+', substring, overlapped=True):
        word = s.group().lower()
        for i in range(10, 21):
            if i > len(word):
                break
            for j in range(len(word) - i + 1):
                if word[j:j + i] == word[j:j + i][::-1]:
                    pals.add(word[j:j + i])
    return pals