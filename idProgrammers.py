def solution(new_id):
    new_id = new_id.lower()

    new_id_list = []
    for i in new_id:
        if
        new_id_list.append(i)

    k = 1
    a = len(new_id_list)

    while k <= a:
        if new_id_list[k - 1] == '.' and new_id_list[k] == '.':
            del new_id_list[k]
            a = len(new_id_list)
        else:
            k += 1

    if new_id_list[0] == '.':
        del new_id_list[0]

    elif new_id_list[len(new_id_list)] == '.':
        del new_id[len(new_id_list)]
    else:
        pass

    if len(new_id_list) == 0:
        new_id_list.append('a')

    if len(new_id_list) <= 2:
        while len(new_id_list) == 3:
            last = new_id_list[len(new_id_list)]
            new_id_list.append[last]

    answer = ''.join(new_id_list)
    print(answer)
    return answer

solution("...!@BaT#*..y.abcdefghijklm")

