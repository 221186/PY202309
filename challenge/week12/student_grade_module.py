import Student # 모듈화한 Student.py를 불러와 Student 내의 함수들을 사용할 수 있게끔 한다.
        

student_info = Student.load_data('student.csv.txt') # loadData에 'student.csv.txt'파일을 넣어 반환된 리스트를 변수에 저장한다.

print('----- 학생들의 평균 점수-----')
for student_ins in student_info:
    student_name = student_ins.name # 학생들의 이름을 저장한다.
    average_grade = student_ins.get_average() # get_averager함수를 통해 평균 성적을 변수에 저장한다.
    print(f'{student_name}의 평균 점수는 {average_grade}입니다.') # 학생들의 평균 성적을 출력한다.

        