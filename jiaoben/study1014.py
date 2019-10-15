from py2neo import Node, Relationship, Graph, NodeMatcher, RelationshipMatcher,walk
graph = Graph('http://localhost:7474', username='neo4j', password='1234567')
'''
for node in graph.nodes:
    print(node)
'''
n=graph.nodes.match('label')
for i in n:
    print(i)
'''
rps=graph.relationships.match('to')

for r in rps:
    print(r)
'''
relationship = graph.match(r_type='to')
print (relationship, type(relationship))
#print(rps.graph.nodenum.)