def if_contains_anagrams(string_list):
    sorted_list = []
    for s in string_list:
        if len(s) >= 3:
            sorted_list.append(''.join(sorted(s.lower())) + ': ' + s.lower())
    count = 0
    for i in range(len(sorted_list)):
        for j in range(i + 1, len(sorted_list)):
            if sorted_list[i][:-3] == sorted_list[j][:-3]:
                count += 1
                if count > 401:
                    return False
    return True