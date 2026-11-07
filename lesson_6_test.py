# # # def juft_sonlar(n):
# # #     # kodingiz shu yerda
# # #     for i in range(n+1):
# # #         if i % 2 == 0:
# # #             yield i

# # # print(list(juft_sonlar(10)))


# # def belgi(func):
# #     # kodingiz shu yerda
# #     def wrapper():
# #         print("--- boshlandi ---")
# #         func()
# #         print("--- tugadi ---")
# #     return wrapper

# # @belgi
# # def salom(ism):
# #     print(f"Salom, {ism}!")

# # salom()

# n = int(input("Son kiriting: "))
# try:
#     int("salom")
# except ValueError:
#     print("Iltimos, son kiriting")
# try:
#     (100 / 0)
# except ZeroDivisionError:
#     print("0 ga bo'lib bo'lmaydi")
# else:
#     print(100 / int(n))



# def baqir(func):
#     # kodingiz shu yerda
#     ...
#     def wrapper(*args, **kwargs):
#         natija = func(*args, **kwargs)
#         return f"{natija.upper()}!!!"
#     return wrapper

# @baqir
# def tanishtir(ism, yosh):
#     return f"men {ism}, {yosh} yoshdaman"

# print(tanishtir("Ali", 20))



# mevalar = ["olma", "nok", "uzum"]
# try:
#     n = int(input("Raqam kiriting: "))
#     mevalar[n]
# except ValueError:
#     print("Iltimos, raqam kiriting")
# except IndexError:
#     print("Bunday raqamli meva yo'q")
# else:
#     print("Siz tanladingiz: ", mevalar[n])
# finally:
#     print("Rahmat, xayr!")





"1"
n, m = map(int, input().split())

def check(func):
    def wrapper(a, b):
        if b == 0:
            return "Denominator can't be zero"
        return func(a, b)
    return wrapper

@check
def divider(a, b):
    return (a / b)

print(divider(n, m))



"2"
def add_employee():
    emp_id = input("ID kiriting: ")
    ism = input("Ism kiriting: ")
    lavozim = input("Lavozim kiriting: ")
    maosh = input("Maosh kiriting: ")
    with open("employees.txt", "a") as f:
        f.write(f"{emp_id}, {ism}, {lavozim}, {maosh}\n")
    print("Xodim qo'shildi ✅")


def view_employees():
    try:
        with open("employees.txt", "r") as f:
            print("ID, Ism, Lavozim, Maosh")
            for line in f:
                print(line.strip())
    except FileNotFoundError:
        print("Hali xodimlar yo'q")


def search_employee():
    emp_id = input("Qidirilayotgan ID: ")
    topildi = False
    try:
        with open("employees.txt", "r") as f:
            for line in f:
                parts = line.strip().split(", ")
                if parts[0] == emp_id:
                    print(f"ID: {parts[0]}")
                    print(f"Ism: {parts[1]}")
                    print(f"Lavozim: {parts[2]}")
                    print(f"Maosh: {parts[3]}")
                    topildi = True
                    break
    except FileNotFoundError:
        print("Hali xodimlar yo'q")
        return
    if not topildi:
        print("Bunday ID yo'q")


def update_employee():
    emp_id = input("O'zgartiriladigan ID: ")
    try:
        with open("employees.txt", "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("Hali xodimlar yo'q")
        return

    topildi = False
    new_lines = []
    for line in lines:
        parts = line.strip().split(", ")
        if parts[0] == emp_id:
            topildi = True
            print("O'zgartirmaslik uchun Enter bosing")
            ism = input(f"Yangi ism ({parts[1]}): ") or parts[1]
            lavozim = input(f"Yangi lavozim ({parts[2]}): ") or parts[2]
            maosh = input(f"Yangi maosh ({parts[3]}): ") or parts[3]
            new_lines.append(f"{emp_id}, {ism}, {lavozim}, {maosh}\n")
        else:
            new_lines.append(line)

    if topildi:
        with open("employees.txt", "w") as f:
            for line in new_lines:
                f.write(line)
        print("Ma'lumot yangilandi ✅")
    else:
        print("Bunday ID yo'q")


def delete_employee():
    emp_id = input("O'chiriladigan ID: ")
    try:
        with open("employees.txt", "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("Hali xodimlar yo'q")
        return

    topildi = False
    new_lines = []
    for line in lines:
        parts = line.strip().split(", ")
        if parts[0] == emp_id:
            topildi = True
        else:
            new_lines.append(line)

    if topildi:
        with open("employees.txt", "w") as f:
            for line in new_lines:
                f.write(line)
        print("Xodim o'chirildi ✅")
    else:
        print("Bunday ID yo'q")


while True:
    try:
        ans = int(input("""
1. Add new employee record
2. View all employee records
3. Search for an employee by Employee ID
4. Update an employee's information
5. Delete an employee record
6. Exit

answer: """))
    except ValueError:
        print("Iltimos raqam kiriting!!!")
        continue

    if ans == 1:
        add_employee()
    elif ans == 2:
        view_employees()
    elif ans == 3:
        search_employee()
    elif ans == 4:
        update_employee()
    elif ans == 5:
        delete_employee()
    elif ans == 6:
        print("Xayr!")
        break
    else:
        print("Enter a correct number please!!!")





"3"
try:
    with open("sample.txt", "r") as f:
        text = f.read()
except FileNotFoundError:
    text = input("Please write a paragraph: ")
    with open("sample.txt", "w") as f:
        f.write(text)

text = text.lower()

arr = []
s = ""
for i in text:
    if i.isalpha():
        s = s + i
    else:
        if s:
            arr.append(s)
            s = ""
if s:
    arr.append(s)

dic = {}
for word in arr:
    if word in dic:
        dic[word] += 1
    else:
        dic[word] = 1

try:
    top_n = int(input("How many top words do you want to see? "))
except ValueError:
    top_n = 5

top = sorted(dic.items(), key=lambda x: x[1], reverse=True)[:top_n]

print(f"Total words: {len(arr)}")
print(f"Top {top_n} most common words:")
for word, count in top:
    if count == 1:
        print(f"{word} - {count} time")
    else:
        print(f"{word} - {count} times")

with open("word_count_report.txt", "w") as f:
    f.write("Word Count Report\n")
    f.write(f"Total Words: {len(arr)}\n")
    f.write(f"Top {top_n} Words:\n")
    for word, count in top:
        f.write(f"{word} - {count}\n")



