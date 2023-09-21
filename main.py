scorelist=[]

def grade_cal(score):
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    elif score >= 50:
        grade = "D"
    else:
        grade = "F"
    return grade 


while True :
    scoreinput = (int(input("ใส่คะแนนนักศึกษา (ใส่เลข 0 เพื่อออกจากการทำงาน) : ")))
    scorelist.append(scoreinput)
    if scoreinput == 0 :
        break

for score in scorelist:
    print("เกรดคุณคือ : ",grade_cal(score))
