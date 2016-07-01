
def name_to_number(name):
    if name == "RK":
        number = 0
    elif name == "SS":
        number = 1
    elif name == "PR":
        number = 2
    return number

def result (un,cn,tn):
    if un == cn:
         resultstg = "Draw"
    elif tn == cn:
       resultstg = "Wins"
    elif tn < cn:
       resultstg = "Lose"
    else:
        resultstg = "Lose"
    return resultstg

def print_result(u_num,c_num,t_num,u_nam,c_chc,c_nam):
    r1= result(u_num,c_num,t_num)
    print (u_nam,r1,c_chc)
    print ("User",r1,c_nam)
    print ('')

user = "PR"
user_number = name_to_number(user)

com1 =("RK")
com2 =("SS")
com3 =("PR")

com_number1 = name_to_number(com1)
com_number2 = name_to_number(com2)
com_number3 = name_to_number(com3)

temp_num = user_number + 1
temp_num %= 3

X1 = print_result(user_number,com_number1,temp_num,user,com1,"Com1")
X2 = print_result(user_number,com_number2,temp_num,user,com2,"Com2")
X3 = print_result(user_number,com_number3,temp_num,user,com3,"Com3")
