import re
with open('task2.html','r',encoding='UTF-8') as f:
    close_tags=set()
    for line in f:
        result=re.findall(r"[<][/][^>]+[>]",line)

        for i in result:
            close_tags.add(i)
print(close_tags)
