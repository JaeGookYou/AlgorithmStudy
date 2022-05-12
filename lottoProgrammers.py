def solution(lottos, win_nums):
    # 1. 0 개수 찾기
    count_0=0
    for a in lottos:
        if a==0:
            count_0+=1

    # 2. 원소 일치 여부 찾기
    count=0
    for i in lottos:
        for j in win_nums:
            if i==j:
                if i!=0 and j!=0:
                    count+=1

    # 3. 순위 선정
    if count==0:
        answer = [7-(count+count_0),6]
    else:
        answer = [7-(count+count_0),7-count]

    print(answer)
    return answer

solution([45, 4, 35, 20, 3, 9],	[20, 9, 3, 45, 4, 35])