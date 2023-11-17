import re
from symbolTable import SymbolTable
from hashTable import HashTable

class ScannerException(Exception):
    pass

class Scanner:
    def __init__(self):
        self.program = None
        self.tokens = []
        self.reservedWords = []
        self.symbolTable = None
        self.PIF = []
        self.index = 0
        self.currentLine = 1
        self.read_tokens()
        self.separators = ["(", ")", "[", "]", ";", ";;", " ", ",", "\t", "\n", "\""]
        self.operators = ["+", "-", "*", "/", "mod", "not", "lt", "le", "eq", "ge", "gt", ">", "<", "->", "?", ":", "=>"]

    def set_program(self, program):
        self.program = program

    def read_tokens(self):
        with open(r"D:\Alex's stuff\005 Scoala\UBB\SemV\Tehnici de Compilare\Lab\LFTC\Lab3\Token.in", "r") as file:
            for line in file:
                parts = line.strip().split(" ")
                if parts[0] in ["var", "fun", "num", "wrd", "arr", "cnum", "cwrd", "true", "false"]:
                    self.reservedWords.append(parts[0])
                else:
                    self.tokens.append(parts[0])

    def create_list_of_program_elements(self):
        try:
            content = self.program
            allSeparators = self.separators + self.operators
            pattern = f'({"|".join(map(re.escape, allSeparators))})'
            tokens = re.split(pattern, content)
            return self.tokenize(tokens)
        except FileNotFoundError:
            return []

    def tokenize(self, tokensToBe):
        resultedTokens = []
        # valueLocationPair = []
        # locationPair = []

        isStringConstant = False
        createdString = ""
        lineNo = 1
        columnNo = 1
        filtered_tokensToBe = [s for s in tokensToBe if s != ""]

        for t in filtered_tokensToBe:
            if t[0] == '"':
                if isStringConstant:
                    createdString = createdString + t
                    locationPair = [lineNo, columnNo]
                    valueLocationPair = [createdString, locationPair]
                    resultedTokens.append(valueLocationPair)
                    createdString = ""
                else:
                    createdString = createdString + t
                isStringConstant = not isStringConstant
                continue
            elif t[0] == '\n':
                lineNo = lineNo + 1
                columnNo = 1
                continue
            else:
                if isStringConstant:
                    createdString = createdString + t
                elif t != " ":
                    locationPair = [lineNo, columnNo]
                    valueLocationPair = [t, locationPair]
                    resultedTokens.append(valueLocationPair)
                    columnNo = columnNo + 1
        return resultedTokens

    # 0 - constants
    # 1 - identifiers
    # 2 - reserved words
    # 3 - operators
    # 4 - separators

    def scan(self, program_file_name):
        try:

            with open(rf"D:\Alex's stuff\005 Scoala\UBB\SemV\Tehnici de Compilare\Lab\LFTC\Lab3\{program_file_name}.txt", "r") as file:
                self.set_program(file.read())

            self.index = 0
            self.PIF = []
            identifiersHashTable = HashTable(20)
            intConstantHashTable = HashTable(20)
            stringConstantHashTable = HashTable(20)
            symbol_table = SymbolTable(20, identifiersHashTable, intConstantHashTable, stringConstantHashTable)
            self.symbolTable = symbol_table

            lexical_error_exists = []
            tokens = self.create_list_of_program_elements()
            if len(tokens) == 0:
                return
            print("------------------------------------------------------------------")

            for entry in tokens:
                token = entry[0]
                if token in self.reservedWords:
                    self.PIF.append([[token, [-1, -1]], 2])
                elif token in self.operators:
                    self.PIF.append([[token, [-1, -1]], 3])
                elif token in self.separators:
                    self.PIF.append([[token, [-1, -1]], 4])
                elif token[0] == "'" and token[len(token) - 1] == "'":
                    index = self.symbolTable.addStringConstant(token)
                    self.PIF.append([["SC", index], 0])
                elif token.isnumeric():
                    index = self.symbolTable.addIntConstant(token)
                    self.PIF.append([["IC", index], 0])
                elif token.isidentifier():
                    index = self.symbolTable.addIdentifier(token)
                    self.PIF.append([["ID", index], 1])

                else:
                    locationPair = entry[1]
                    lexical_error_exists.append(
                        f"Error at line {locationPair[0]}, word {locationPair[1]}, invalid token {token} \n")
                    # raise ScannerException(f"Error at line {locationPair[0]} and column {locationPair[1]}, invalid token {token}")

        except (IOError, ScannerException) as e:
            print(str(e))
        if len(lexical_error_exists) == 0:
            print("Program is lexically correct!")
            with open("PIF" + program_file_name + ".out", "w") as file_writer:
                for pair in self.PIF:
                    file_writer.write(f"token: {pair[0][0]} --at: {pair[0][1]}  type-> ({pair[1]})\n")

            with open("ST" + program_file_name + ".out", "w") as file_writer:
                file_writer.write(self.symbolTable.toString())
        else:
            for error in lexical_error_exists:
                print(error)

    def getPIF(self):
        return self.PIF

    def getSymbolTable(self):
        return self.symbolTable