def processLine(line):
    grades = []
    current = ""
    for char in line:
        if char == '$':
            grades.append(current)
            current = ""
        else:
            current += char
    if current:
        grades.append(current)
    return grades

def gradeToNumber(grade):
    numberGrade = 0
    if grade[0]=='A':
        numberGrade = 95
    elif grade[0]=='B':
        numberGrade = 85
    elif grade[0]=='C':
        numberGrade = 75
    elif grade[0]=='D':
        numberGrade = 65
    elif grade[0]=='F':
        numberGrade = 50

    if len(grade)>1 and grade[1]=='+':
        numberGrade+=0.3
    if len(grade)>1 and grade[1]=='-':
        numberGrade-=0.3
    return numberGrade

# This is probably the least efficient way I could do this, but that didn't stop me
# Additional comment from after I finished writing, this IS the least efficient way I could've done it
def numberToGrade(grade):
    if grade>=95.3:
        return 'A+'
    elif grade>=94.7:
        return 'A'
    elif grade>=90:
        return 'A-'
    elif grade>=85.3:
        return 'B+'
    elif grade>=84.7:
        return 'B'
    elif grade>=80:
        return 'B-'
    elif grade>=75.3:
        return 'C+'
    elif grade>=74.7:
        return 'C'
    elif grade>=70:
        return 'C-'
    elif grade>=65.3:
        return 'D+'
    elif grade>=64.7:
        return 'D'
    elif grade>=60:
        return 'D-'
    else:
        return 'F'

def gradeReport(grades, dropped, average, finalGrade):
    print("----------------------------------------")
    print("|         GRADE REPORT SUMMARY         |")
    print("----------------------------------------")
    print(f"| Grades Entered: {', '.join(grades):<21}|")
    print(f"| Lowest Grade Dropped: {dropped:<14} |")
    print(f"| Calculated Average: {average:>7.2f}          |")
    print(f"| Final Letter Grade:   {finalGrade:<14} |")
    print("----------------------------------------")