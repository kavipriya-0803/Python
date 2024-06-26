1. Widgets and Gizmos
An online retailer sells two products: widgets and gizmos. Each widget weighs 75 grams. Each gizmo weighs 112 grams. Write a program that reads the number of widgets and the number of gizmos from the user. Then your program should compute and display the total weight of the parts.

Sample Input
10
20
Sample Output
The total weight of all these widgets and gizmos is 2990 grams.
For example:
Input	Result
10
20	
The total weight of all these widgets and gizmos is 2990 grams.
PROGRAM:
a=int(input())
b=int(input())
print("The total weight of all these widgets and gizmos is",((a*75)+(b*112)),"grams.")

2. Doll Sings
In London, every year during Dasara there will be a very grand doll show. People try to invent new dolls of different varieties. The best-sold doll's creator will be awarded with a cash prize. So people broke their heads to create dolls innovatively. Knowing this competition, Mr.Lokpaul tried to create a doll that sings only when an even number is pressed and the number should not be zero and greater than 100.
IF Lokpaul wins print true, otherwise false.

Sample Input
10
Sample Output
True
Explanation:
Since 10 is an even number and a number between 0 and 100, True is printed
PROGRAM:
a=int(input())
if(a>0 and a<100 and a%2==0):
    print("True")
else:
    print("False")

3. Birthday Party
Mr. X's birthday is in next month. This time he is planning to invite N of his friends. He wants to distribute some chocolates to all of his friends after the party. He went to a shop to buy a packet of chocolates. At the chocolate shop, 4 packets are there with different numbers of chocolates. He wants to buy such a packet which contains a number of chocolates, which can be distributed equally among all of his friends. Help Mr. X to buy such a packet.

Input Given: 
N-No of friends
P1,P2,P3 AND P4-No of chocolates
OUTPUT:
 "True" if he can buy that packet and "False" if he can't buy that packet.
SAMPLE INPUT AND OUTPUT:
5
25
12  
10  
9
OUTPUT
True False True False
PROGRAM:
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
print(b%a==0,c%a==0,d%a==0,e%a==0)

4.Hamming Weight
Write a python program that takes a integer between 0 and 15 as input and displays the number of '1' s in its binary form.(Hint:use python bitwise operator.
Sample Input
3
Sample Output:
2
Explanation:
The binary representation of 3 is 011, hence there are 2 ones in it. so the output is 2.
PROGRAM:
a=int(input())
n=bin(a)
n=n.replace("0b","")
s=str(n)
c=list(s)
d=0
for i in range(len(c)):
    if(int(c[i])==1):
        d+=1
print(d)

5. Compound Interest
Pretend that you have just opened a new savings account that earns 4 percent interest per year. The interest that you earn is paid at the end of the year, and is added to the balance of the savings account. Write a program that begins by reading the amount of money deposited into the account from the user. Then your program should compute and display the amount in the savings account after 1, 2, and 3 years. Display each amount so that it is rounded to 2 decimal places.
Sample Input:
10000
Sample Output:
Balance as of end of Year 1: $10400.00.
Balance as of end of Year 2: $10816.00.
Balance as of end of Year 3: $11248.64
PROGRAM:
a=int(input())
b=(a*0.04)+a
c=b+(b*0.04)
d=c+(c*0.04)
print("Balance as of end of Year 1: ${:.2f}.".format(b))
print("Balance as of end of Year 2: ${:.2f}.".format(c))
print("Balance as of end of Year 3: ${:.2f}.".format(d))

6. Eligible to donate blood
A team from the Rotract club had planned to conduct a rally to create awareness among the Coimbatore people to donate blood. They conducted the rally successfully. Many of the Coimbatore people realized it and came forward to donate their blood to nearby blood banks. The eligibility criteria for donating blood are people should be above or equal to 18 and his/ her weight should be above 40. There was a huge crowd and staff in the blood bank found it difficult to manage the crowd. So they decided to keep a system and ask the people to enter their age and weight in the system. If a person is eligible he/she will be allowed inside.
 Write a program and feed it to the system to find whether a person is eligible or not.

Input Format:
Input consists of two integers that correspond to the age and weight of a person respectively.
Output Format:
Display True(IF ELIGIBLE)
Display False (if not eligible)
Sample Input
19
45
Sample Output
True
PROGRAM:
a=int(input())
b=int(input())
if(a>=18 and b>40):
    print("True")
else:
    print("False")

7. C or D
Mr.Ram has been given a problem kindly help him to solve it. The input of the program is either 0 or 1. IF 0 is the input he should display "C" if 1 is the input it should display "D".There is a constraint that Mr. Ram should use either logical operators or arithmetic operators to solve the problem, not anything else.
Hint:
Use ASCII values of C and D.

Input Format:
An integer x, 0<=x<=1. .
Output Format:
output a single character "C" or "D"  depending the value of x. 
Input 1:
0
Output 1:
C

Input 2:
1

Output 1:
D
PROGRAM:
a=int(input())
if(a==0):
    print("C")
else:
    print("D")

8. Troy Battle
In the 1800s, the battle of Troy was led by Hercules. He was a superstitious person. He believed that his crew can win the battle only if the total count of the weapons in hand is in multiple of 3 and the soldiers are in an even number of count. Given the total number of weapons and the soldier's count, Find whether the battle can be won or not according to Hercules's belief. If the battle can be won print True otherwise print False.
Input format:
Line 1 has the total number of weapons
Line 2 has the total number of Soldiers.
Output  Format:
If the battle can be won print True otherwise print False.

Sample Input:
32
43
Sample Output:'
False

a=int(input())
b=int(input())
if(a%3==0 and b%2==0):
    print("True")
else:
    print("False")

9. Tax and Tip
The program that you create for this exercise will begin by reading the cost of a meal ordered at a restaurant from the user. Then your program will compute the tax and tip for the meal. Use your local tax rate (5 percent) when computing the amount of tax owing. Compute the tip as 18 percent of the meal amount (without the tax). The output from your program should include the tax amount, the tip amount, and the grand total for the meal including both the tax and the tip. Format the output so that all of the values are displayed using two decimal places.
Sample Input
100
Sample Output
The tax is 5.00 and the tip is 18.00, making the total 123.00
PROGRAM:
a=int(input())
print("The tax is {:.2f} and the tip is {:.2f}, making the total {:.2f}".format((a*0.05),(a*0.18),(a+((a*0.05)+(a*0.18)))))

10. Return last digit of the given number
Write a program that returns the last digit of the given number. Last digit is being referred to the least significant digit i.e. the digit in the ones (units) place in the given number.
The last digit should be returned as a positive number.
For example,
if the given number is 197, the last digit is 7
if the given number is -197, the last digit is 7
For example:
Input	Result
123	3
PROGRAM:
a=int(input())
print(abs(a)%10)


 
