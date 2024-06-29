'''
Database
# RDBMS
RDBMS(SQL)은 행/열의 생김새가 정해진 엑셀에 데이터를 저장하는 것과 유사합니다. 
데이터 50만 개가 적재된 상태에서, 갑자기 중간에 열을 하나 더하기는 어렵지만, 
정형화되어 있는 만큼 데이터가 일관적이고 분석에 용이합니다. 
MS-SQL, My-SQL 등이 여기에 속하죠.

# NoSQL
NoSQL은 딕셔너리 형태로 데이터를 저장해두는 DB로, 
데이터 하나하나 마다 같은 필드 값들을 가질 필요가 없어 
자유로운 형태의 데이터 적재에 유리한 대신, 일관성이 부족할 수 있습니다. 
우리가 쓸 MongoDB가 이에 속합니다.
'''
from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:jungle@cluster0.gsunejv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client.dbsparta

# doc = {
#     'name':'영수',
#     'age':24
# }

# db.users.insert_one(doc)

# 'users'라는 collection에 {'name':'bobby','age':21}를 넣습니다.
# db.users.insert_one({'name':'영희','age':30})
# db.users.insert_one({'name':'철수','age':20})
# db.users.insert_one({'name':'john','age':30})

# 모든 데이터 뽑아보기
all_users = list(db.users.find({},{'_id':False}))

print(all_users[0])         # 0번째 결과값을 보기
print(all_users[0]['name']) # 0번째 결과값의 'name'을 보기

for a in all_users:      # 반복문을 돌며 모든 결과값을 보기
    print(a)

user = db.users.find_one({})
print(user)

# 오타가 많으니 이 줄을 복사해서 씁시다!
db.users.update_one({'name':'영수'},{'$set':{'age':19}})

user = db.users.find_one({'name':'영수'})
print(user)

db.users.delete_one({'name':'영수'})

user = db.users.find_one({'name':'영수'})
print(user)


# 저장 - 예시
doc = {'name':'bobby','age':21}
db.users.insert_one(doc)

# 한 개 찾기 - 예시
user = db.users.find_one({'name':'bobby'})

# 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
same_ages = list(db.users.find({'age':21},{'_id':False}))

# 바꾸기 - 예시
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

# 지우기 - 예시
db.users.delete_one({'name':'bobby'})