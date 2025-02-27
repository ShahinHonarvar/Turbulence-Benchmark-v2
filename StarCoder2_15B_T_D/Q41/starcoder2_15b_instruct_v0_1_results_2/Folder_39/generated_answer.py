def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    identical = set()
    for i in range(len(list1)):
        if 20 <= i <= 30 and list1[i] == list2[i]:
            identical.add(list1[i])
    return identical