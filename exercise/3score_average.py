kor_score = [49,79,20,100,80]
math_score = [43,59,85,30,90]
eng_score = [49,79,48,60,100]

midterm_score = [kor_score, math_score, eng_score]
#print(midterm_score)
#print(midterm_score[0][2])

student_score = [0,0,0,0,0]
i = 0
for subject in midterm_score:
    for score in subject:
        student_score[i] += score
        i+=1
    #print(student_score)
    i = 0 #과목이 바뀔 때 학생 인덱스 초기화 (!!놓친 부분)
else:
    print(f'학생별 합산 점수는 {student_score} 입니다.')
    # 평균 계산 (unpacking)
    a,b,c,d,e = student_score
    student_average = [int(a/3),int(b/3),int(c/3),int(d/3),int(e/3)]
    print(f'학생별 평균 점수는 {student_average} 입니다.')

    

