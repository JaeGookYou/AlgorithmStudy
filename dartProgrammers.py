def solution(dartResult):
    new_list = list(dartResult)

    for j in range(1,len(dartResult)):
        if new_list[j-1]=='1' and dartResult[j]=='0':
            new_list[j-1]='10'
            del new_list[j]

    print(new_list)
    tmp=[]
    count=0
    for i in range(len(new_list)):
        try:
            a=int(new_list[i])
        except:
            if new_list[i]=='S':
                new_list[i]=1
                a=a**new_list[i]

            elif new_list[i]=='D':
                new_list[i]=2
                a=a**new_list[i]

            elif new_list[i]=='T':
                new_list[i]=3
                a=a**new_list[i]

            elif new_list[i]=='#':
                a=a*(-1)

            elif new_list[i]=='*':

            tmp.append(a)

            
    print(tmp)

    answer = 0
    return answer
solution('1T2D3D#')