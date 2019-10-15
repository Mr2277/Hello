from py2neo import Graph, Node, Relationship

graph = Graph("http://localhost:7474", username="neo4j", password='password')
graph.delete_all()

'''
    1 —— 创建node，函数第一个参数是节点类型，第二个参数是value值
'''
a = Node('PersonTest', name='张三')
b = Node('PersonTest', name='李四')
r = Relationship(a, 'KNOWNS', b)
s = a | b | r
graph.create(s)

'''
    2　——　Node查询
'''
# 用CQL进行查询，返回的结果是list
data1 = graph.data('MATCH(p:PersonTest) return p')
print("data1 = ", data1, type(data1))
print()
# 用find_one()方法进行node查找，返回的是查找node的第一个node
data2 = graph.find_one(label='PersonTest', property_key='name', property_value="李四")
print("data2 = ", data2, type(data2))
print()
# 用find()方法进行node查找
data3 = graph.find(label='PersonTest')
for data in data3:
    print("data3 = ", data)
print()
'''
    3　——　Relationship查询
'''
relationship = graph.match_one(rel_type='KNOWNS')
print(relationship, type(relationship))
print()

'''
    4 —— 更新Node的某个属性值，若node没有该属性，则新增该属性
'''
node1 = graph.find_one(label='PersonTest', property_key='name', property_value="张三")
node1['age'] = 21
graph.push(node1)
data4 = graph.find(label='PersonTest')
for data in data4:
    print("data4 = ", data)
print()

node1['age'] = 99
graph.push(node1)
data5 = graph.find(label='PersonTest')
for data in data5:
    print("data5 = ", data)
print()

'''
    5 —— 删除某node，在删除node之前需要先删除relationship
'''
node = graph.find_one(label='PersonTest', property_key='name', property_value="李四")
relationship = graph.match_one(rel_type='KNOWNS')
graph.delete(relationship)
graph.delete(node)
data6 = graph.find(label='PersonTest')
for data in data6:
    print("data6 = ", data)

'''
    6 —— 多条件查询
'''
a = Node('PersonTest', name='张三', age=21, location='广州')
b = Node('PersonTest', name='李四', age=22, location='上海')
c = Node('PersonTest', name='王五', age=21, location='北京')
r1 = Relationship(a, 'KNOWS', b)
r2 = Relationship(b, 'KNOWS', c)
s = a | b | c | r1 | r2
graph.create(s)
data7 = graph.find(label='PersonTest')
for data in data7:
    print("data7 = ", data)
print()
'''
# 单条件查询，返回的是多个结果
selector = NodeSelector(graph)
persons = selector.select('PersonTest', age=21)
print("data8 = ", list(persons))
print()

# 多条件查询
selector = NodeSelector(graph)
persons = selector.select('PersonTest', age=21, location='广州')
print("data9 = ", list(persons))
print()

# orderby进行更复杂的查询
selector = NodeSelector(graph)
persons = selector.select('PersonTest').order_by('_.age')
for data in persons:
    print("data10 = ", data)
print()
'''