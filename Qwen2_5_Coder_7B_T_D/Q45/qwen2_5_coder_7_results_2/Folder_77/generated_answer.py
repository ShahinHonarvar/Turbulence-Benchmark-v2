def palindromes_between_indices(s: str) -> set:
    letters = s[4:7].lower()
    letters_set = set(letters)
    length = len(letters)
    if length < 4:
        return set()
    palindromes = set()
    for i in range(4 - length + 1):
        for j in range(i + length, 5):
            for k in range(j + length, 6):
                for l in range(k + length, 7):
                    for m in range(l + length, 8):
                        for n in range(m + length, 9):
                            for o in range(n + length, 10):
                                for p in range(o + length, 11):
                                    char_list = list(letters)
                                    char_list.append(s[i])
                                    char_list.append(s[j])
                                    char_list.append(s[k])
                                    char_list.append(s[l])
                                    char_list.append(s[m])
                                    char_list.append(s[n])
                                    char_list.append(s[o])
                                    char_list.append(s[p])
                                    char_list.sort()
                                    palindrome = ''.join(char_list)
                                    if palindrome == palindrome[::-1]:
                                        palindromes.add(palindrome)
    return palindromes