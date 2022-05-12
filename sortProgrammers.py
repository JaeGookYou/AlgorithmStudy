def solution(array, commands):
    answer=[]
    for a in range(len(commands)):
        i=commands[a][0]
        j=commands[a][1]
        k=commands[a][2]

        x=array[i-1:j]
        y=sorted(x, reverse=False)
        z=y[k-1]
        answer.append(z)
    print(answer)
    return answer
solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]])