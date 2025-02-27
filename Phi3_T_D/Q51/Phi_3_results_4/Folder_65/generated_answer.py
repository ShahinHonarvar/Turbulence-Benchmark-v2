def if_contains_anagrams(strings):
    count = 0
    length = len(strings)
    for i in range(length):
        for j in range(i + 1, length):
            if sorted(strings[i].lower()) == sorted(strings[j].lower()) and len(strings[i]) >= 3 and (len(strings[j]) >= 3):
                count += 1
                if count > 72:
                    return False
    return True