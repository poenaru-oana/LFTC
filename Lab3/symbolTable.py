from hashTable import KeyValuePair, HashTable


class SymbolTable:
    def __init__(self, size, identifiersHashTable: HashTable, intConstantsHashTable: HashTable,
                 stringConstantsHashTable: HashTable):
        self.size = size
        self.identifiersHashTable = identifiersHashTable
        self.intConstantsHashTable = intConstantsHashTable
        self.stringConstantsHashTable = stringConstantsHashTable

    def get_size(self):
        return self.size

    def addIdentifier(self, identifier):
        return self.identifiersHashTable.add(identifier)

    def addIntConstant(self, constant):
        return self.intConstantsHashTable.add(constant)

    def addStringConstant(self, constant):
        return self.stringConstantsHashTable.add(constant)

    def hasIdentifier(self, identifier):
        return self.identifiersHashTable.contains(identifier)

    def hasIntConstant(self, identifier):
        return self.intConstantsHashTable.contains(identifier)

    def hasStringConstant(self, identifier):
        return self.stringConstantsHashTable.contains(identifier)

    # def findPositionIdentifier(self, identifier):
    #     return self.identifiersHashTable.contains(identifier)

    # def findPositionIntConstant(self, constant):
    #     return self.intConstantsHashTable.contains(constant)

    # def findPositionStringConstant(self, constant):
    #     return self.stringConstantsHashTable.contains(constant)

    def toString(self):
        return " IDENTIFIERS: \n " + self.identifiersHashTable.toString() + " INT CONSTANTS: \n " + self.intConstantsHashTable.toString() + " STRING CONSTANTS: \n " + self.stringConstantsHashTable.toString()
