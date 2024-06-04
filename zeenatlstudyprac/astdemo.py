import ast
import pprint

code = '''
def greet(name,age):
    print("Hello, " + name + age)
    
        print()
    
greet("John")
'''

tree = ast.parse(code)
pprint.pprint(ast.dump(tree))