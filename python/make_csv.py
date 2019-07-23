
students = {
    '01' : '김성훈',
    '02' : '김은정',
    '03' : '김태우'
}



with open('a.csv', 'w', encoding = 'utf-8') as f:
    f.write('number, name\n')
    for number, name in students.items():
        f.write(f'{number}, {name}\n')






# with open('a.csv', 'w', encoding = 'utf-8') as f:
#     for i in range(5):
#         f.write(f'{i}hi\n') 





# # 이렇게도 할 수 있지만, 좀 더 쉽게 해주는게 있는데! 그게바로 밑에꺼
#------------------------------------------------------------------------------

import csv
students = {
    'anything': {
        '순번':'01',
        '이름':'김성훈'
    },
    'anything2': {
        '순번':'02',
        '이름':'김은정'
    }
}

# with open('b.csv','w',encoding='utf-8') as f:
#     csv_writer = csv.writer(f)
#     for item in students.items():
#         csv_writer.writerow(item)
# # 이것도 조금 불편해
# #-----------------------------------------------------------------------------
# import csv
# with open('b.csv','w',encoding='utf-8') as f:
#     fieldnames = ['순번', '이름']  # 여기만 변경하면 될걸
#     csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
#     csv_writer.writeheader()
#     for item in students.values():
#         csv_writer.writerow(item)
#위의 코드를 계속 쓴다고 생각하면되고 딕셔너리를 어떻게 만드느냐가 중요


# students2 = [
#     {
#         '순번' : '02',
#         '이름' : '김은정',

#     },
#     {
#         '순번' : '03',
#         '이름' : '김인성'
#     }

# ]
# 딕셔너리를 student 처럼도 되지만 위에꺼처럼 해도 된다고는 하시는데...
# import csv
# with open('c.csv','w',encoding='utf-8') as f:
#     fieldnames = ['순번', '이름']  # 여기만 변경하면 될걸
#     csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
#     csv_writer.writeheader()
#     csv_writer.writerow(students2[0])



# 딕셔너리 통째로 넣으면 되는건지, 넣으면 알아서 filedname에 맞는것만 뽑아주는건지 
