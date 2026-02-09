import grade_compute

def main():
    print("Enter 4 grades seperated by $ (do not include spaces):")
    grades = input().upper()
    gradeList = grade_compute.processLine(grades)
    
    # Computing average
    lowest = 100
    averageGrade=0
    curveCount = 0
    for grade in gradeList:
        temp = grade_compute.gradeToNumber(grade)
        averageGrade+=temp
        if temp<lowest:
            lowest = temp
        if temp<74.7:
            curveCount+=1
    
    averageGrade = (averageGrade-lowest)/3
    if curveCount>=3:
        averageGrade+=0.25
    finalGrade = grade_compute.numberToGrade(averageGrade)

    grade_compute.gradeReport(gradeList, grade_compute.numberToGrade(lowest), averageGrade, finalGrade)

if __name__ ==  "__main__":
    main()