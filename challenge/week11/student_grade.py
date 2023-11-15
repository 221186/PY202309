class student(): # student라는 클래스를 만들고 name,kor,math,eng라는 인스턴스를 만든다.
    name = ''
    kor = 0
    math = 0
    eng = 0

    
    def get_average(self): # get_average 메소드를 통해 student 클래스에 있는 
        return (self.kor + self.math + self.eng) / 3 # 과목 3개를 self(student)로 받아 평균을 구하는 함수를 설정한다.


def load_data(file_name): 
    student_info = [] # 학생들의 이름과 성적을 저장할 리스트를 만든다.
    # file_name에 있는 문장들을 한 문장씩 리스트로 lines에 저장한다.
    lines = open(file_name, "r", encoding="utf8").readlines() 

    for line in lines:
        students_info = line.replace('\n', '').split(',') # 학생들 정보에 끝에 '\n'을 없애고 ','을 기준으로 토큰화 한다.

        student_ins = student() # student_ins 변수에 student 클래스를 할당한다.
        student_ins.name = students_info[0] # 학생들의 이름을 student 클래스의 name에 저장한다. 
        student_ins.kor = float(students_info[1]) # 학생들의 국어 성적을 student 클래스의 kor에 저장한다. 
        student_ins.math = float(students_info[2]) # 학생들의 수학 성적을 student 클래스의 math에 저장한다. 
        student_ins.eng = float(students_info[3]) # 학생들의 영어 성적을 student 클래스의 eng에 저장한다. 

        student_info.append(student_ins) # 학생들의 정보를 리스트에 추가한다.

    return student_info
        

student_info = load_data('student.csv.txt') # loadData에 'student.csv.txt'파일을 넣어 반환된 리스트를 변수에 저장한다.

print('----- 학생들의 평균 점수-----')
for student_ins in student_info:
    student_name = student_ins.name # 학생들의 이름을 저장한다.
    average_grade = student_ins.get_average() # get_averager함수를 통해 평균 성적을 변수에 저장한다.
    print(f'{student_name}의 평균 점수는 {average_grade}입니다.') # 학생들의 평균 성적을 출력한다.
