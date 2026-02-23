import matplotlib.pyplot as plt

student_names = ["Shanjay","Kartik","Hareshan","Danial","Ajay","Priya","Karen","Jandel"]
student_marks = [45,47,39,35,45,30,49,31]

#Plotting graph
plt.plot(student_names,student_marks)
plt.xlabel("Student name")
plt.ylabel("Student marks")
plt.show()

marks_pers = []
for i in student_marks:
  res =(i/50) * 100
  marks_pers.append(res)

plt.bar(student_names,marks_pers)
plt.xlabel("Student name")
plt.ylabel("Student marks")
plt.show()


import numpy as np

xpoints = np.array([1,8])
ypoints = np.array([3,10])
plt.plot(xpoints,ypoints,'o')
plt.show()

ypoints = np.array([3,8,1,10])
plt.plot(ypoints,marker='d',mec='y',ms=20,linestyle='dashed',color='green')
plt.show()