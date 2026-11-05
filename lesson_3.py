"1"
arr = list(input())
n = input()
print(arr.count(n))

"2"
arr = list(map(int, input().split()))
print(sum(arr))

"3"
arr = list(map(int, input().split()))
print(max(arr))

"4"
arr = list(map(int, input().split()))
print(min(arr))

"5"
arr = list(map(int, input().split()))
n = int(input())
if n in arr:
    print("YES")
else:
    print("NO")

"6"
arr = list(map(int, input().split()))
if len(arr) == 0:
    print("nothing in here")
else:
    print(arr[0])

"7"
arr = list(map(int, input().split()))
if len(arr) == 0:
    print("nothing in here")
else:
    print(arr[-1])

"8"
arr = list(map(int, input().split()))
arr1 = arr[:3]
print(arr1)

"9"
arr = list(map(int, input().split()))
arr1 = arr[::-1]
print(arr1)

"10"
arr = list(map(int, input().split()))
arr1 = sorted(arr)
print(arr1)

"11"
arr = list(map(int, input().split()))
arr1 = set(arr)
print(arr1)

"12"
arr = list(map(int, input().split()))
n = input()
a = int(input("index: "))
arr.insert(a, n)
print(arr)

"13"
arr = list(map(int, input().split()))
n = input()
print(arr.index(n))

"14"
arr = list(map(int, input().split()))
if len(arr) == 0:
    False
else:
    True

"15"
arr = list(map(int, input().split()))
for i in arr:
    if i % 2 == 0:
        print(i, end=" ")

"16"
arr = list(map(int, input().split()))
for i in arr:
    if i % 2 != 0:
        print(i, end=" ")

"17"
arr = list(map(int, input().split()))
arr1 = list(map(int, input().split()))
arr.extend(arr1)
print(arr)

"18"
arr = list(map(int, input().split()))
sublist = list(map(int, input().split()))
if sublist in arr:
    print("YES")
else:
    print("NO")

"19"
a = list(map(int, input().split()))
x = int(input())
y = int(input())
if x in a:
    i = a.index(x)
    a[i] = y
print(a)

"20"
a = list(map(int, input().split()))
a.sort()
print(a[-2])

"21"
a = list(map(int, input().split()))
a.sort()
print(a[1])

"22"
a = list(map(int, input().split()))
b = []
for i in a:
    if i % 2 == 0:
        b.append(i)
print(b)

"23"
a = list(map(int, input().split()))
b = []
for i in a:
    if i % 2 != 0:
        b.append(i)
print(b)

"24"
a = list(map(int, input().split()))
print(len(a))

"25"
a = list(map(int, input().split()))
b = a.copy()
print(b)

"26"
a = list(map(int, input().split()))
k = len(a)
if k % 2 != 0:
    print(a[k // 2])
else:
    print(a[k // 2 - 1], a[k // 2])

"27"
a = list(map(int, input().split()))
s = int(input())
e = int(input())
print(max(a[s:e]))

"28"
a = list(map(int, input().split()))
s = int(input())
e = int(input())
print(min(a[s:e]))

"29"
a = list(map(int, input().split()))
idx = int(input())
a.pop(idx)
print(a)

"30"
a = list(map(int, input().split()))
print(a == sorted(a))

"31"
a = list(map(int, input().split()))
n = int(input())
b = []
for i in a:
    for _ in range(n):
        b.append(i)
print(b)

"32"
x = list(map(int, input().split()))
y = list(map(int, input().split()))
z = sorted(x + y)
print(z)

"33"
a = list(map(int, input().split()))
x = int(input())
b = []
for i in range(len(a)):
    if a[i] == x:
        b.append(i)
print(b)

"34"
a = list(map(int, input().split()))
k = int(input())
if len(a) > 0:
    k %= len(a)
else:
    k = 1
b = a[-k:] + a[:-k]
print(b)

"35"
s = int(input())
t = int(input())
a = []
for i in range(s, t + 1):
    a.append(i)
print(a)

"36"
a = list(map(int, input().split()))
s = 0
for i in a:
    if i > 0:
        s += i
print(s)

"37"
a = list(map(int, input().split()))
s = 0
for i in a:
    if i < 0:
        s += i
print(s)

"38"
a = list(map(int, input().split()))
print("YES" if a == a[::-1] else "NO")

"39"
a = list(map(int, input().split()))
sz = int(input())
b = []
for i in range(0, len(a), sz):
    b.append(a[i:i + sz])
print(b)

"40"
a = list(map(int, input().split()))
b = []
for i in a:
    if i not in b:
        b.append(i)
print(b)

"Tusple tasks"

"1"
t = tuple(map(int, input().split()))
n = int(input())
print(t.count(n))

"2"
t = tuple(map(int, input().split()))
print(max(t))

"3"
t = tuple(map(int, input().split()))
print(min(t)) 

"4"
t = tuple(map(int, input().split()))
n = int(input())
if n in t:
    print("YES")
else:
    print("NO")

"5"
t = tuple(map(int, input().split()))
print(t[1])

"6"
t = tuple(map(int, input().split()))
print(t[-1])

"7"
t = tuple(map(int, input().split()))
print(len(t))

"8"
t = tuple(map(int, input().split()))
t1 = t[:3]
print(t1)

"9"
t = tuple(map(int, input().split()))
t1 = tuple(map(int, input().split()))
t.extend(t1)
print(t)

"10"
t = tuple(map(int, input().split()))
if len(t) == 0:
    print("nothing in here")
else:
    True

"11"
t = tuple(map(int, input().split()))
x = int(input())
b = []
for i in range(len(t)):
    if t[i] == x:
        b.append(i)
print(tuple(b))

"12"
t = tuple(map(int, input().split()))
l = list(t)
l.sort()
print(l[-2])

"13"
t = tuple(map(int, input().split()))
l = list(t)
l.sort()
print(l[1])

"14"
x = input()
t = (x,)
print(t)

"15"
a = list(map(int, input().split()))
t = tuple(a)
print(t)

"16"
t = tuple(map(int, input().split()))
print(t == tuple(sorted(t)))

"17"
t = tuple(map(int, input().split()))
s = int(input())
e = int(input())
print(max(t[s:e]))

"18"
t = tuple(map(int, input().split()))
s = int(input())
e = int(input())
print(min(t[s:e]))

"19"
t = tuple(map(int, input().split()))
x = int(input())
l = list(t)
if x in l:
    l.remove(x)
print(tuple(l))

"20"
t = tuple(map(int, input().split()))
sz = int(input())
b = []
for i in range(0, len(t), sz):
    b.append(tuple(t[i:i + sz]))
print(tuple(b))

"21"
t = tuple(map(int, input().split()))
n = int(input())
b = []
for i in t:
    for _ in range(n):
        b.append(i)
print(tuple(b))

"22"
s = int(input())
e = int(input())
b = []
for i in range(s, e + 1):
    b.append(i)
print(tuple(b))

"23"
t = tuple(map(int, input().split()))
print(t[::-1])

"24"
t = tuple(map(int, input().split()))
print("YES" if t == t[::-1] else "NO")

"25"
t = tuple(map(int, input().split()))
b = []
for i in t:
    if i not in b:
        b.append(i)
print(tuple(b))

"Set tasks"
"1"
s = set(map(int, input().split()))
s1 = set(map(int, input().split()))
s2 = s.union(s1)
print(s2)

"2"
s = set(map(int, input().split()))
s1 = set(map(int, input().split()))
s2 = s.intersection(s1)
print(s2)

"3"
s = set(map(int, input().split()))
s1 = set(map(int, input().split()))
s2 = s.difference(s1)
print(s2)

"4"
s = set(map(int, input().split()))
subset = set(map(int, input().split()))
if subset in s:
    print("YES")
else:
    print("NO") 

"5"
s = set(map(int, input().split()))
n = int(input())
if n in s:
    print("YES")
else:
    print("NO") 

"6"
s = set(map(int, input().split()))
print(len(s))

"7"
arr = list(map(int, input().split()))
s = set(arr)
print(s)

"8"
s = set(map(int, input().split()))
x = int(input())
if x in s:
    s.remove(x)
print(s)

"9"
s = set(map(int, input().split()))
s = set()
print(s)

"10"
s = set(map(int, input().split()))
if len(s) == 0:
    print(True)
else:
    print(False)

"11"
a = set(map(int, input().split()))
b = set(map(int, input().split()))
c = a.symmetric_difference(b)
print(c)

"12"
s = set(map(int, input().split()))
x = int(input())
s.add(x)
print(s)

"13"
s = set(map(int, input().split()))
if len(s) > 0:
    x = s.pop()
    print(x)
else:
    print("Set bo'sh")

"14"
s = set(map(int, input().split()))
print(max(s))

"15"
s = set(map(int, input().split()))
print(min(s))

"16"
s = set(map(int, input().split()))
b = set()
for i in s:
    if i % 2 == 0:
        b.add(i)
print(b)

"17"
s = set(map(int, input().split()))
b = set()
for i in s:
    if i % 2 != 0:
        b.add(i)
print(b)

"18"
x = int(input())
y = int(input())
s = set()
for i in range(x, y + 1):
    s.add(i)
print(s)

"19"
a = list(map(int, input().split()))
b = list(map(int, input().split()))
s = set(a + b)
print(s)

"20"
a = set(map(int, input().split()))
b = set(map(int, input().split()))
print(a.isdisjoint(b))

"21"
a = list(map(int, input().split()))
s = set(a)
b = list(s)
print(b)

"22"
a = list(map(int, input().split()))
s = set(a)
print(len(s))

"23"
import random

n = int(input())
mn = int(input())
mx = int(input())
s = set()
for _ in range(n):
    s.add(random.randint(mn, mx))
print(s)

"Dictionary tasks"
"1"
d = {"a": 1, "b": 2}
k = input()
if k in d:
    print(d[k])
else:
    print("nothin in here")

"2"
d = {"a": 1, "b": 2}
k = input()
print(k in d)

"3"
d = {"a": 1, "b": 2, "c": 3}
print(len(d))

"4"
d = {"a": 1, "b": 2}
b = []
for i in d.keys():
    b.append(i)
print(b)

"5"
d = {"a": 1, "b": 2}
b = []
for i in d.values():
    b.append(i)
print(b)

"6"
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}
d3 = {}
for k, v in d1.items():
    d3[k] = v
for k, v in d2.items():
    d3[k] = v
print(d3)

"7"
d = {"a": 1, "b": 2}
k = input()
if k in d:
    d.pop(k)
print(d)

"8"
d = {"a": 1, "b": 2}
d = {}
print(d)

"9"
d = {"a": 1}
print(len(d) == 0)

"10"
d = {"a": 1, "b": 2}
k = input()
if k in d:
    print(k, d[k])
else:
    print("nothin in here")

"11"
d = {"ism": "Ali", "yosh": 25}
k = input()
v = input()
d[k] = v
print(d)

"12"
d = {"a": 1, "b": 2, "c": 1}
x = int(input())
c = 0
for v in d.values():
    if v == x:
        c += 1
print(c)

"13"
d = {"a": 1, "b": 2}
b = {}
for k, v in d.items():
    b[v] = k
print(b)

"14"
d = {"a": 1, "b": 2, "c": 1}
x = int(input())
b = []
for k, v in d.items():
    if v == x:
        b.append(k)
print(b)

"15"
k_list = input().split()
v_list = input().split()
d = {}
for i in range(len(k_list)):
    d[k_list[i]] = v_list[i]
print(d)

"16"
d = {"a": 1, "b": {"x": 10}}
has_nested = False
for v in d.values():
    if type(v) == dict:
        has_nested = True
print(has_nested)

"17"
d = {"user": {"name": "Ali", "age": 25}}
print(d["user"]["name"])

"18"
from collections import defaultdict
d = defaultdict(lambda: "Topilmadi")
d["ism"] = "Ali"
print(d["ism"])
print(d["yosh"])

"19"
d = {"a": 1, "b": 2, "c": 1}
b = set(d.values())
print(len(b))

"20"
d = {"b": 2, "a": 1, "c": 3}
b = {}
for k in sorted(d.keys()):
    b[k] = d[k]
print(b)

"21"
d = {"b": 2, "a": 1, "c": 3}
b = {}
for k, v in sorted(d.items(), key=lambda i: i[1]):
    b[k] = v
print(b)

"22"
d = {"a": 10, "b": 5, "c": 20}
limit = int(input())
b = {}
for k, v in d.items():
    if v > limit:
        b[k] = v
print(b)

"23"
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
has_common = False
for k in d1.keys():
    if k in d2:
        has_common = True
print(has_common)

"24"
t = (("a", 1), ("b", 2))
d = {}
for k, v in t:
    d[k] = v
print(d)

"25"
d = {"a": 1, "b": 2}
for k in d:
    print((k, d[k]))
    break