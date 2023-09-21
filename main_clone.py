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

coll = int(input("ใส่จำนวนนักศึกษา : "))

for i in range(coll):
    scorelist.append(int(input(f"ใส่คะแนนนักศึกษา {i+1} : ")))

for score in scorelist:
    print("เกรดของคุณคือ : ",grade_cal(score))
