#Jaunel Deans
#Oct 5, 2023
#Ask the user to enter the values for sides A, B, C, D, and E and print out the total room area.


sideA = int(input("Enter side A: "))#Input for sideA
sideB = int(input("Enter side B: "))#Input for sideB
sideC = int(input("Enter side C: "))#Input for sideC
sideD = int(input("Enter side D: "))#Input for sideD
sideE = int(input("Enter side E: "))#Input for sideE

#Divided the shape into 4 different shapes. 

shape1 = (sideB * sideC)#shape1 was a rectangle. Length * Width

shape2 = ((sideA-sideC) * sideB)#shape2 was a rectangle. The Area is length * width. To find the width of the rectangle you subtract the measurements of sideC from sideA. Then you multipy by sideB. 

shape3 = (0.5*sideE*(sideA-sideC))#shape3 was a triangle. The area of a triangle is 0.5*b*h. You multiply the difference of sideA and sideC with 0.5 and sideE

shape4 = (((sideD-sideE)-sideB)*(sideA-sideC))#shape4 is a rectangle. The Area is length * width. You have to multiply the difference of sideD, sideE and sideB by the difference of sideA and sideC



totalArea = shape1+shape2+shape3+shape4#Add all the areas together to find the area of the total shape. 

print()
print("Room Area: " + str(totalArea))#Display the area of the shape. 