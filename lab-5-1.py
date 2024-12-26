import re
import html

with open('task1-en.txt','r') as f:
    capital_let=[]
    colon_end=[]

    for line in f:
        result_lp=re.findall(r"[A-ZА-Я][A-Za-zА-Яа-я]+",line)
        for i in result_lp:
            capital_let.append(i)

        line_changed=re.sub(r"[A-ZА-Я][A-Za-zА-Яа-я]+",'',line)

        result_lp_1=re.findall(r"[A-ZА-Я]",line_changed)
        for  i in result_lp_1:
            capital_let.append(i)

        result_lp_2=re.findall(r"[A-Za-zА-Яа-я]+[:]",line)

        for i in result_lp_2:
            colon_end.append(i)

print(capital_let)
print(colon_end)