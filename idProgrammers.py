def solution(new_id):
    new_id = new_id.lower()
    print("1: " + new_id)

    new_id_list = []
    for i in new_id:
        try:
            int(i)
            new_id_list.append(i)
        except:
            if i.isalpha() == True:
                new_id_list.append(i)
            else:
                if i == '.' or i == '_' or i == '-':
                    new_id_list.append(i)
                else:
                    continue
    print("2: " , new_id_list)

    k = 1
    temp_list = new_id_list
    while k < len(temp_list):
        if new_id_list[k-1] == new_id_list[k] and new_id_list[k-1] == '.':
            del new_id_list[k]
            temp_list = new_id_list
            continue
        else:
            k += 1
            continue
    new_id_list = temp_list
    print("3: ", new_id_list)
    
    if new_id_list[0] == '.':
        del new_id_list[0]
    elif new_id_list[len(new_id_list)-1] == '.':
        del new_id_list[len(new_id_list)-1]
    print("4: " , new_id_list)

    if len(new_id_list) == 0:
        new_id_list.append('a')
    print("5: " , new_id_list)

    temp2_list = []
    if len(new_id_list) >= 16:
        for l in range(15):
            temp2_list.append(new_id_list[l])
        if temp2_list[14] == '.':
            del temp2_list[len(temp2_list)-1]
        new_id_list = temp2_list
    print("6: ", new_id_list)

    if len(new_id_list) <= 2:
        print(new_id_list[len(new_id_list) - 1])
        x = new_id_list[len(new_id_list)-1]
        while len(new_id_list) <= 2:
            new_id_list.append(x)
    print("7: ", new_id_list)

    answer = ''.join(new_id_list)
    print(answer)
    return answer

solution("=.=")

