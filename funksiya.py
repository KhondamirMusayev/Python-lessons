# while True:
#     def raqam(nomer):
#         if nomer > 0:
#             return True
#     a = int(input("Sonni kiriting = "))
#     if raqam(a):
#         print("Bu son musbat")
#     else:
#         print("Bu son musbat emas")
# def nomer(raqam):
#     if raqam % 2 != 0:
#         return True
# a = int(input("Sonni kiriting = "))
# if nomer(a):
#     print("Bu son toq son")
# else:
#     print("Bu son juft son")
# def raqam(nomer):
#     if nomer % 2 == 0:
#         return True
# a = int(input("Sonni kiriting = "))
# if raqam(a):
#     print("Son juft son")
# else:
#     print("Son toq son")
# while True:
#     ism = input("Ismni kiriting = ")
#     if ism == "Xondamir":
#         print("Boshqa ism kiriting")
#     else:
#         print("Ism kiritildi")
# def avto_info(kompaniya,model,**malumotlar):
#     """Avto haqidagi ma'lumotlarni lug'at ko'rinishdia qaytaruvchi funksiya"""
#     malumotlar['kompaniya']=kompaniya
#     malumotlar['model']=model
#     return malumotlar
# avto1 = avto_info("GM", "malibu", rang='qora', yil=2018)
# avto2 = avto_info("Kia", "K5", rang='qizil', narh=35000)
# print(avto2)

# def kopaytirish(*son):
#     kopaytma = 1
#     for i in son:
#         kopaytma *= i
#     return kopaytma
# print(kopaytirish(4,5,6))

# def talaba(**malumot):
#     return malumot
# print(talaba(ismi = "Xondamir",familya = "Musayev",yosh = "13"))
# a = int(input("Son kiriting = "))
# b = int(input("Son kiriting = "))
# c = int(input("Son kiriting = "))
# print(sorted(a,b,c))
# sonlar = []
# a = int(input("Son kirit = "))
# for i in range(a):
#     son = int(input((i+1)))