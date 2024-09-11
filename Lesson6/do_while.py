#for
#while
#do-while

#input 3 grades
#calculate avg
#(grade1 + grade2 + grade3) /3
#do it until all grades are different
#all grades are between 0-100
#avg is more than 85

while True:
    grade1: int = int(input("grade1"))
    grade2: int = int(input("grade2"))
    grade3: int = int(input("grade3"))
    sum_grades = grade1 + grade2 + grade3
    avg_grades = sum_grades / 3
    is_valid_grade1 = 0<= grade1 <= 100
    is_valid_grade2 = 0<= grade2 <= 100
    is_valid_grade3 = 0<= grade3 <= 100

    if is_valid_grade1 and is_valid_grade2 and is_valid_grade3\
            and avg_grades > 85 and not grade1 == grade2 == grade3:
            break