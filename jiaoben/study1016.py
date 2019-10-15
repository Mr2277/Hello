from py2neo import Graph, Node, Relationship,RelationshipMatcher

graph = Graph("http://localhost:7474", username="neo4j", password='1234567')
#graph.delete_all()

'''
    1 —— 创建node，函数第一个参数是节点类型，第二个参数是value值
'''

a = Node('PersonTest', name='张三')
b = Node('PersonTest', name='李四')
r = Relationship(a, 'KNOWNS', b)
s = a | b | r
graph.create(s)

a = Node('PersonTest', name='王五')
b = Node('PersonTest', name='赵六')
r = Relationship(a, 'NOKNOWNS', b)
s = a | b | r
graph.create(s)

relMatch = RelationshipMatcher(graph)
relList = list(relMatch.match())
for i in relList:
    print(i)    # 查找图数据库中所有关系