def solution(s):
    temp = []
    i = 0
    while i < len(s):
        try:
            int(s[i])
            print(s[i])
            temp.append(s[i])
            i += 1
        except:
            if s[i] == 'z':
                temp.append('0')
                i += 4
                continue
            elif s[i] == 'o':
                temp.append('1')
                i += 3
                continue
            elif s[i] == 't':
                if s[i+1] == 'w':
                    temp.append('2')
                    i += 3
                    continue
                else:
                    temp.append('3')
                    i += 5
                    continue
            elif s[i] == 'f':
                if s[i+1] == 'o':
                    temp.append('4')
                    i += 4
                    continue
                else:
                    temp.append('5')
                    i += 4
                    continue
            elif s[i] == 's':
                if s[i+1] == 'i':
                    temp.append('6')
                    i += 3
                    continue
                else:
                    temp.append('7')
                    i += 5
                    continue
            elif s[i] == 'e':
                temp.append('8')
                i += 5
                continue
            elif s[i] == 'n':
                temp.append('9')
                i += 4
                continue

    print(temp)
    str_ans = ''.join(temp)
    answer = int(str_ans)
    return answer

solution("one4seveneight")