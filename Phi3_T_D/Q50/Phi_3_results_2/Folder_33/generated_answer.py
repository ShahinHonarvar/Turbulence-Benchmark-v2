def if_contains_anagrams(strings):
    count = 0
    for i in range(len(strings)):
        wo_t = tuple(sorted(strings[i].lower()))
        for j in range(i + 1, len(strings)):
            if wo_t == tuple(sorted(strings[j].lower())):
                count += 1
            if count >= 140:
                return True
    return False