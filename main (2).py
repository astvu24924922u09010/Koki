yclass student:                         def__int__(self,name,             roll_number,cgpa):
  self.name=name
  self.roll_number=roll_number
  self.cgpa=cgpa
  def sort_students(student_list):
sorted_students=sorted(student_list,key=lambda student:
   student.cgpa,reverse=True)
  return sorted_students  
student=[
    Student("Hari","A123",7.8),
    Student("Srikanth","A124",8.9),
    Student("Soumya","A125",9.1),
    Student("mahendra","A126",9.9),
  ]
sorted_students=sort_students(students)
for studet in sorted_students:
Print("name:{},roll number:{},CGPA:{}"
format(student.name,student.roll_number,Student:cgpa))

  
  