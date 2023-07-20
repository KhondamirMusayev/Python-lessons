# x1 = int(input("1-uchi x koordinatasini kiriting: "))
# y1 = int(input("1-uchi y koordinatasini kiriting: "))
# x2 = int(input("2-uchi x koordinatasini kiriting: "))
# y2 = int(input("2-uchi y koordinatasini kiriting: "))
# x3 = int(input("3-uchi x koordinatasini kiriting: "))
# y3 = int(input("3-uchi y koordinatasini kiriting: "))

# if x1 == x2:
#     x4 = x3
# elif x1 == x3:
#     x4 = x2
# else:
#     x4 = x1

# if y1 == y2:
#     y4 = y3
# elif y1 == y3:
#     y4 = y2
# else:
#     y4 = y1

# print("To'rtinchi uchi koordinatasi:", x4, y4)
# x = int(input("Nuqta x koordinatasini kiriting: "))
# y = int(input("Nuqta y koordinatasini kiriting: "))

# if x == 0:
#     if y > 0:
#         chorak = "OX"
#     else:
#         chorak = "-OX"
# elif y == 0:
#     if x > 0:
#         chorak = "OY"
#     else:
#         chorak = "-OY"
# else:
#     chorak = "Koordinata o'qida joylashmaydi"

# print("Nuqta koordinata choragi:", chorak)
# x = int(input("X koordinatasini kiriting: "))
# y = int(input("Y koordinatasini kiriting: "))

# if x == 0 and y == 0:
#     print(0)
# elif x == 0 or y == 0:
#     print(1)
# else:
#     print(3)
#     A = int(input("A nuqtaga masofani kiriting: "))
# B = int(input("B nuqtaga masofani kiriting: "))
# C = int(input("C nuqtaga masofani kiriting: "))

# if abs(A) <= abs(B) and abs(A) <= abs(C):
#     eng_yaqin_nuqta = "A"
#     masofa = abs(A)
# elif abs(B) <= abs(A) and abs(B) <= abs(C):
#     eng_yaqin_nuqta = "B"
#     masofa = abs(B)
# else:
#     eng_yaqin_nuqta = "C"
#     masofa = abs(C)

# print("Eng yaqin nuqta:", eng_yaqin_nuqta)
# print("Masofa:", masofa)
# son1 = int(input("1-sonni kiriting: "))
# son2 = int(input("2-sonni kiriting: "))
# son3 = int(input("3-sonni kiriting: "))
# son4 = int(input("4-sonni kiriting: "))

# if son1 == son2 == son3:
#     tartib = 4
# elif son1 == son2 == son4:
#     tartib = 3
# elif son1 == son3 == son4:
#     tartib = 2
# else:
#     tartib = 1

# print("Tartib raqami:", tartib)
son1 = int(input("1-sonni kiriting: "))
son2 = int(input("2-sonni kiriting: "))
son3 = int(input("3-sonni kiriting: "))

if son1 == son2:
    tartib = 3
elif son1 == son3:
    tartib = 2
else:
    tartib = 1

print("Tartib raqami:", tartib)