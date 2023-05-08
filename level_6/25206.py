score = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0,
         "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0}
product_sum = 0.0
credit_sum = 0.0
for _ in range(20):
    course, credit, grade = map(str, input().split())
    if grade != "P":
        credit_sum += float(credit)
        product_sum += float(credit) * score[grade]
gpa = product_sum/credit_sum
print(gpa)