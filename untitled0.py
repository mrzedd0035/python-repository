# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 23:45:40 2021

@author: mrzed
"""

def main():

    students = []
   
    fp = open('./student.csv','r')
    lines = fp.readlines()
    fp.close()
   
    for line in lines:
        line = line.strip()  
        items = line.split(',')
       
        student = {}
        student['id'] = int(input())
        student['name'] = int (input())
        student['중간고사'] = int(input())
        student['기말고사'] = int(input())
        student['기본점수'] = int(input())
        student['total'] = 0
        student['avg'] = 0.0
        student['ranking'] = 0
       
        students.append(student)
       
    for student in students:
        student['total'] = student['중간고사'] + student['기말고사'] + student['']
        student['avg'] = student['total'] / 3   
          
    sorted_students = sorted(students, key = lambda x : x['total'], reverse=True)

    count = 1
    for student in sorted_students:
        student['ranking'] = count
        count = count + 1
       
    result_students = sorted(sorted_students, key = lambda x : x['id'])
   
    fp = open('./result_student.csv', 'w')
   
    for student in result_students:
        line = ','.join([str(student['id']),str(student['name']),str(student['중간']),str(student['기말고사']),
                         str(student['기본점수']),str(student['total']),str(student['avg']),str(student['ranking']),'\n'])
        fp.write(line)
       
    fp.close()
       
    for student in sorted_students:
        print(student)
    
if __name__ == "__main__":
    main()
