print("Welcome!")
name = input("What is your name?\n")
tutor_group = input("What is your tutor group?\n")
print("Lets start with your grades")
obj1 = str("\nTo develop a knowledge and understanding of "+input("Enter the objective name\n"))
grade11 = int(input("Enter the first grade of the objective\t"))
grade12 = int(input("Enter the second grade of the objective\t"))
grade13 = int(input("Enter the third grade of the objective\t"))
print("\n\tNow Objective 2:\n")

obj2 = str("\nTo develop a knowledge and understanding of "+input("Enter the objective name\n"))
grade21 = int(input("Enter the first grade of the objective\t"))
grade22 = int(input("Enter the second grade of the objective\t"))
grade23 = int(input("Enter the third grade of the objective\t"))

grade1 = [grade11,grade12,grade13]
sorted1 = sorted(grade1)
highest1 = sorted1[len(grade1)-1]
grade2 = [grade21,grade22,grade23]
sorted2 = sorted(grade2)
highest2 =sorted2[len(grade2)-1]
#average1 = sum(grade1) / float(len(grade1))
average1 = (highest1+highest2)/2
#average2 = sum(grade2) / float(len(grade2))
print("{0}'s total average is {1} and their highest grade for Objective 1 was {2}\nFor Objective 2 ther highest grade was {3}".format(name,average1,highest1,highest2))
