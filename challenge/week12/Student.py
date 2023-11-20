class Student(): # student라는 클래스를 만들고
    
    def __init__(self, name, kor, math, eng): # 생성자를 이용해 자동으로 클래스 내 변수를 생성한다.
        self.name = name # 학생들의 이름 변수 생성
        self.kor = kor # 학생들의 국어 성적 변수 생성
        self.math = math # 학생들의 수학 변수 생성
        self.eng = eng # 학생들의 영어 변수 생성
    
    def get_average(self): # get_average 메소드를 통해 student 클래스에 있는 
        return (self.kor + self.math + self.eng) / 3 # 과목 3개를 self(student)로 받아 평균을 구하는 함수를 설정한다.


def load_data(file_name): 
    student_info = [] # 학생들의 이름과 성적을 저장할 리스트를 만든다.
    # file_name에 있는 문장들을 한 문장씩 리스트로 lines에 저장한다.
    lines = open(file_name, "r", encoding="utf8").readlines() 

    for line in lines:
        students_info = line.replace('\n', '').split(',') # 학생들 정보에 끝에 '\n'을 없애고 ','을 기준으로 토큰화 한다.

        student_ins = Student(students_info[0], # Student 클래스의 객체들을 생성한다
                              float(students_info[1]), 
                              float(students_info[2]),
                              float(students_info[3])) 
        
        student_info.append(student_ins) # 학생들의 정보를 리스트에 추가한다.

    return student_info