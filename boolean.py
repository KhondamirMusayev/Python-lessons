# --------------------------1 masala-------------------
# while True:
#     def raqam(nomer):
#         if nomer > 0:
#             return True
#     a = int(input("Sonni kiriting = "))
#     if raqam(a):
#         print("Bu son musbat")
#     else:
#         print("Bu son musbat emas")
# -------------------------2 masala----------------------
# def nomer(raqam):
#     if raqam % 2 != 0:
#         return True
# a = int(input("Sonni kiriting = "))
# if nomer(a):
#     print("Bu son toq son")
# else:
#     print("Bu son juft son")
# --------------------------3 masala----------------------------
# def raqam(nomer):
#     if nomer % 2 == 0:
#         return True
# a = int(input("Sonni kiriting = "))
# if raqam(a):
#     print("Son juft son")
# else:
#     print("Son toq son")
# --------------------------4 masala------------------------------
# a = int(input())
# b = int(input())
# if a>2:
#     print(True)
# else:
#     print(False)
# if b<=3:
#     print(True)
# else:
#     print(False)
# ---------------------------5 masala-----------------------------
# A = -1
# B = -3
# javob = A >= 0 or B < -2
# print(javob)
# ---------------------------6 masala-----------------------------
# A = 3
# B = 5
# C = 7
# javob = A <= B <= C
# print(javob)
# ---------------------------9 masala-----------------------------
# a = int(input("Son kiriting = "))
# b = int(input('Son kiriting = '))
# c = int(input("Son kiriting = "))
# if c == :
#     print("A juft son")
# else:
#     print("A toq son")
# if b%2==0:
#     print("B juft son")
# else:
#     print("B toq son")
a = int(input("Son kiriting = "))
b = int(input("Son kiriting = "))
c = int(input("Son kiriting = "))
musbat_sonlar = 0
manfiy_sonlar = 0
for son in a,b,c:
    if son > 0:
        musbat_sonlar += 1
    elif son < 0:
        manfiy_sonlar += 1
print(f"Musbat sonlar = {musbat_sonlar},Manfiy sonlar = {manfiy_sonlar}")