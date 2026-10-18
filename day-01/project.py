##Updated
def result(marks):
    total = sum(marks)
    average = total / len(marks)
    
    if average > 90:
        print("Excellent")
    elif average>70:
        print("Normal")
    elif average > 50:
        print("Needs improvement")
    else:
        print("Bad Result")
        
    print("Marks:")
    for i in marks:
        print(i)
    
    print("Total :", total)
    print("Avg: ", average)
    

student_marks = [45, 100, 97, 34, 45]

result(student_marks)
