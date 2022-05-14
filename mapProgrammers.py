def solution(n, arr1, arr2):
    # 1. sharp를 옮겨 담기 위한 빈 배열 생성
    shp = []

    new_shp = []
    for k in range(n):
        new_shp.append(0)

    # 2. 단계별로 sharp와 빈칸 채우기
    for i in range(n):
    # 2-1. 배열의 원소를 이진수로 변환
        b1 = format(arr1[i],'b')
        b2 = format(arr2[i],'b')

    # 2-2. 빈칸이 있으면 0으로 채움
        if len(b1) < n:
            b1 = b1.zfill(n)

        if len(b2) < n:
            b2 = b2.zfill(n)

    # 2-3. 조건에 따른 sharp 채워 넣기
        for j in range(n):
            if b1[j] == b2[j] and b1[j] == "0":
                shp.append(" ")
            else:
                shp.append("#")

    # 2-6. 공백 겹치면 삭제
        for l in range(1,n):
            if shp[l-1] == " " and shp[l] == " ":
                del shp[l-1]


    # 2-4. shp의 sharp와 공백을 합치기
        shp_line = ''.join(shp)

    # 2-5. 합친 모양을 배열에 저장 후 shp초기화
        new_shp[i] = shp_line

        shp = []

    answer = new_shp
    return answer

solution(5, [9, 20, 28, 18, 11],[30, 1, 21, 17, 28])
solution(6,[46, 33, 33 ,22, 31, 50],[27 ,56, 19, 14, 14, 10])
