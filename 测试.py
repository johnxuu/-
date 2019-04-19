#  打印一个边长为n的正方形
#边长用*代替
n = int(input("请输入正方形的边长"))
print("* "*n)
for i in range(n-2):
    print("*"," "*(n-2),"*")
print("*"*n)

# 求100以内所有奇数的和    答案（2500）
n = 0
for i in range(1,101):
    if i%2 ==1:
        n+=i
print(n)


#判断学生成绩，成绩等级A~E，其中，90分以上为A，80~89分为b，70~79分为c，60~69分为d，60分以下为e


a = int(input("成绩"))
if a<0:
    print("请重新输入")
else:
    if a >= 90:
        print("A")
    elif a >= 80:
        print("B")
    elif a >= 70:
        print("C")
    elif a >= 60:
        print("D")
    else:
        print("E")

# 求1到5的阶乘之和  答案 153
n = 0
m = 1
for i in range(1,6): 
    m = m*i
    n+=m
print(n)



#给一个数，判断是否质数     注意2的特殊性
a = int(input("yigeshu"))
for i in range(2,a):
    if a%i==0:
        print(a,"不是质数")
        break
else:
    print(a)


#获取100以内的质数
num=[];
i=2
for i in range(2,100):
   j=2
   for j in range(2,i):
      if(i%j==0):
         break
   else:
      num.append(i)
print(num)


# 九九乘法表
for i in range(1,10):
  k = 1
  for k in range(1,i+1):
    print('{}x{}={}\t'.format(k,i,i*k),end=" ")
  print()


#打印一个菱形
n = 4
for i in range(1,8,2):
  n-=1 
  print(" "*n,"*"*i)
for j in range(5,0,-2):
  n+=1
  print(" "*n,"*"*j)


#打印菱形      只能是奇数
line = int(input(""))
for i in range(-line//2,line//2+1):      # i 是空格数
    if i <=0:
      print(" "*(-i),"*"*(line-2*(-i)))
    else:
      print(" "*(i),"*"*(line-2*(i)))


#打印100以内的斐波那契数列
list = []
a,b=0,1
while b in range(0,1000000000000):
  print(b)
  a,b= b,a+b 


#求斐波那契数列101项
i = 0 
j = 1
c = 1

while True:
  num = i+j
  i=j
  j = num
  c+=1
  if c==101:
    print(num)



# 对角线打印九九乘法表

for i in range(1,10):
  s = ""
  m = ""
  
  for j in range(1,10):
    n = 0
    if j>=i:
      s += "{}*{}={:<5}".format(i,j,i*j)
    else:
      m += "{}*{}={:<5}".format(i,j,i*j)
      n+=1
      print("         "*n,end="")
  print(s)


# 1给一个半径，求圆的面积和周长，圆周率3.14
a = int(input("半径"))
print("圆的面积={}".format(3.14*a**2))
print("圆的周长={}".format(3.14*a*2))
# 2输入2个数，比较大小后，从小到大升序打印
b = int(input("第一个数"))
c= int(input("第二个数"))
if b>=c:
  print(c,b)
else:
  print(b,c)
# 3获取最大值，请输入若干个整数，打印出最大值
list = []
while True:
  b = input("")
  if b=="":
    break
  else:
    list.append(int(b))
print("最大的数是：",max(list))

  # 冒泡法
n = 0
count = 0  # 交换次数
zzz= 0  #循环次数
list = [1,9,8,5,6,7,4,3,2]
for i in range(len(list)):
    
    for j in range(len(list)-i-1):
        zzz+=1
        if list[j]<list[j+1]:
            continue
        else:
            no1 = list[j]
            list[j] = list[j+1]
            list[j+1] = no1
            count+=1
            
            
print(list)
print(zzz)
print(count)



# 最大公约数
a = int(input('请输入一个数'))
b = int(input('请输入一个数'))
if a >b:
    smil = b
else:
    smil =a

for i in range(1,smil+1):
    if a%i==0 and b%i==0:
        c = i
print(c)


# 返回2个数的最小公倍数
a = int(input('请输入一个数'))
b = int(input('请输入一个数'))

if a >b:
    smil = b
else:
    smil =a

for i in range(1,smil+1):
    if a%i==0 and b%i==0:
        c = i
d=a*b/c
print(d)
