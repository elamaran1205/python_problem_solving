import argparse

students = {}
parser = argparse.ArgumentParser()
parser.add_argument("--data",nargs="+",help="Enter name and mark",required=True)
cla_argument = parser.parse_args()

students = {cla_argument.data[i]:int(cla_argument.data[i+1]) for i in range(0,len(cla_argument.data),2)}

print(students)

topper = max(students,key=students.get)
top_mark = max(students.values())
print(f"Highest scorer: {topper},Mark - {top_mark}")

avg = sum(students.values())/len(students)
print(f"Average score of students: {avg}")

print("\nAll students Marks:") 
for name, mark in students.items():
    print(f"{name:10} - {mark}")

