#!/usr/bin/env python
# coding: utf-8

# In[6]:


for x in range(1) :

    NAME = input("학생 이름을 입력하시오 : ")

    A = int(input("중간 점수 : ")) # 중간 30%
    B = int(input("기말 점수 : ")) # 기말 30%
    C = int(input("기본 점수 : ")) # 기본 40% / 13

    D = A + B + C
    E = D/3

print(NAME,"학생","중간",A,"기말",B,"기본",C,"합",int(D))

if E >= 30:
    print("A")
elif 25 <= E < 30:
    print("B")
elif 20 <= E < 25:
    print("C")
elif 15 <= E < 20:
    print("D")
else:
    print("E")


# In[ ]:





# In[ ]:




