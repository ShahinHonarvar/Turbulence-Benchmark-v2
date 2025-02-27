def all_substring_of_size_n(s):
    result = set()
    length = len(s)
    if length < 65:
        return list(result)
    for i in range(length - 64):
        temp = set()
        for j in range(65):
            if s[i + j] not in temp:
                temp.add(s[i + j])
            else:
                break
        if len(temp) == 65:
            result.add(''.join(sorted(temp)))
    return list(result)