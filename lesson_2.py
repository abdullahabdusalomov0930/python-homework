"1"
a = float(input("a = "))
print("a = ", f"{a:.2f}")

"2"
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
print(max(a, b, c))
print(min(a, b, c))

"3"
n = int(input("how many kilometers: "))
print(f"{n} kilometers = {n * 1000} meters")
print(f"{n} kilometers = {n * 100000} centimeters")

"4"
a = int(input("a = "))
b = int(input("b = "))
print(a // b)
print(a % b)

"5"
c = float(input("celsius = "))
f = c * 1.8 + 32
print("fahrenheit =", f)

"6"
n = int(input("number = "))
print(n % 10)

"7"
n = int(input("n = "))
print(n % 2 == 0)


# STRING

"1"
name = input("name: ")
year = int(input("birth year: "))
print(name, 2026 - year)

"2"
txt = 'LMaasleitbtui'
print(txt[::2])
print(txt[1::2])

"3"
s = input("text: ")
print(len(s))
print(s.upper())
print(s.lower())

"4"
word = input("word: ")
print(word == word[::-1])

"5"
text = input("text: ").lower()
v = 0
c = 0
for i in text:
    if i in "aeiou":
        v += 1
    elif i.isalpha():
        c += 1
print("vowels:", v, "consonants:", c)

"6"
s1 = input("text 1: ")
s2 = input("text 2: ")
print(s2 in s1)

"7"
gap = input("sentence: ")
eski = input("replace: ")
yangi = input("with: ")
print(gap.replace(eski, yangi))

"8"
s = input("string: ")
print(s[0], s[-1])

"9"
s = input("string: ")
print(s[::-1])

"10"
gap = input("sentence: ")
print(len(gap.split()))

"11"
s = input("string: ")
has_digit = False
for i in s:
    if i.isdigit():
        has_digit = True
print(has_digit)

"12"
words = ["apple", "banana", "cherry"]
print("-".join(words))

"13"
s = input("text: ")
print(s.replace(" ", ""))

"14"
a = input("first: ")
b = input("second: ")
print(a == b)

"15"
gap = input("sentence: ").split()
res = ""
for w in gap:
    res += w[0].upper()
print(res)

"16"
s = input("text: ")
harf = input("char: ")
print(s.replace(harf, ""))

"17"
s = input("text: ")
for i in "aeiouAEIOU":
    s = s.replace(i, "*")
print(s)

"18"
gap = input("input: ")
boshi = input("starts with: ")
oxiri = input("ends with: ")
print(gap.startswith(boshi) and gap.endswith(oxiri))


# BOOLEAN

"1"
login = input("username: ")
parol = input("password: ")
print(login != "" and parol != "")

"2"
a = int(input("a = "))
b = int(input("b = "))
if a == b:
    print("teng")

"3"
n = int(input("n = "))
print(n > 0 and n % 2 == 0)

"4"
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
print(a != b and b != c and a != c)

"5"
s1 = input("s1 = ")
s2 = input("s2 = ")
print(len(s1) == len(s2))

"6"
n = int(input("n = "))
print(n % 3 == 0 and n % 5 == 0)

"7"
a = float(input("a = "))
b = float(input("b = "))
print(a + b > 50)

"8"
n = int(input("n = "))
print(10 <= n <= 20)