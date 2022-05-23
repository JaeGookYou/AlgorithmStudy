def solution(new_id):
    new_id = new_id.lower()

    print(new_id)

    new_id_list = []
    num = []
    for j in range(10):
        num.append(j)

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
            
    print(new_id_list)
    answer = new_id_list
    return answer

solution("...!@BaT#*..y.abcdefghijklm")

