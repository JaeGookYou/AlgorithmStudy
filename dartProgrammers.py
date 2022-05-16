def solution(dartResult):
    new_list = list(dartResult)

    for j in range(1,len(dartResult)):
        if new_list[j-1]=='1' and dartResult[j]=='0':
            new_list[j-1]='10'
            del new_list[j]

    print(new_list)

    for k in new_list:
        try:
            a=int(k)
        except:




    answer = 0
    return answer
solution('1D2S#10S')