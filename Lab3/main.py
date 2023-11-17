from symbolTable import SymbolTable
from hashTable import KeyValuePair, HashTable
from scanner import Scanner

# identifiersHashTable = HashTable(20)
# intConstantHashTable = HashTable(20)
# stringConstantHashTable = HashTable(20)
# symbolTable = SymbolTable(20,identifiersHashTable,intConstantHashTable,stringConstantHashTable)

# identifier1 = KeyValuePair("a",4)
# identifier2 = KeyValuePair(20 ,10)
# identifier3 = KeyValuePair("a" ,23)
# identifier4 = KeyValuePair("c" ,23)

# symbolTable.addIdentifier(identifier1)
# symbolTable.addIdentifier(identifier2)
# symbolTable.addIdentifier(identifier3)

# print(symbolTable.hasIdentifier(identifier1))
# print(symbolTable.hasIdentifier(identifier2))
# print(symbolTable.hasIdentifier(identifier3))
# print(symbolTable.hasIdentifier(identifier4))

scanner = Scanner()
scanner.scan("p1")
scanner.scan("p2")
scanner.scan("p3")
scanner.scan("perr")
