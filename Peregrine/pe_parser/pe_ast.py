"""
*  
*  Copyright (c) Peregrine-lang, 2021. All rights reserved.
*
"""

from typing import List

from lexer.tokens import Token,TokenType

class Node:
    def __str__(self) -> str:
        pass

class Program(Node):
    nodes: List[Node] = []

    def __str__(self) -> str:
        result = ""

        for node in self.nodes:
            result += node.__str__()

        return result

class IntegerLiteral(Node):
    value: str

    def __init__(self, value: str) -> None:
        self.value = value

    def __str__(self) -> str:
        return self.value

class DecimalLiteral(Node):
    value: str

    def __init__(self, value: str) -> None:
        self.value = value

    def __str__(self) -> str:
        return self.value

class StringLiteral(Node):
    value: str

    def __init__(self, value: str) -> None:
        self.value = value

    def __str__(self) -> str:
        return self.value

class BoolLiteral(Node):
    value: bool

    def __init__(self, value: bool) -> None:
        self.value = value

    def __str__(self) -> str:
        return "True" if self.value else "False"

class Identifier(Node):
    value: str

    def __init__(self, value: str) -> None:
        self.value = value

    def __str__(self) -> str:
        return self.value

class BinaryOperation(Node):
    left: Node
    operator: str
    right: Node

    def __init__(self, left: Node, operator: str, right: Node) -> None:
        self.left = left
        self.operator = operator
        self.right = right

    def __str__(self) -> str:
        return f"({self.left.__str__()} {self.operator} {self.right.__str__()})"

class PrefixExpression(Node):
    prefix: str
    value: Node

    def __init__(self, prefix: str, value: Node) -> None:
        self.prefix = prefix
        self.value = value

    def __str__(self) -> str:
        return f"({self.prefix}{self.value.__str__()})"

class VariableDeclaration(Node):
    varType: Token
    varName: str
    value: Node

    def __init__(self, varType: Token, varName: str, value: Node = None) -> None:
        self.varType = varType
        self.varName = varName
        self.value = value

    def __str__(self) -> str:
        return f"( {self.varType.keyword} ( {self.varName} = {str(self.value)} ) )"

class VariableReassignment(Node):
    varName: str
    newValue: Node

    def __init__(self, varName: str, newValue: Node) -> None:
        self.varName = varName
        self.newValue = newValue

    def __str__(self) -> str:
        return f"({self.varName} = {str(self.newValue)})"



class logical_Statement(Node):
    condition: Node
    then_branch: Node

    # def __init__(self, condition: Node, then_branch: Node, else_branch: Node) -> None:
    def __init__(self,statement:str, condition: Node, then_branch: Node) -> None:
        self.condition = condition
        self.then_branch = then_branch
        # self.else_branch = else_branch
        self.statement_type:str=statement

    
    def __str__(self) -> str:
        #original
        #i commented it out because it is adding if statement even whene none are available
        # return "(if" + "(" + self.condition.__str__() + ")) " + self.then_branch.__str__() + " " + "else " + self.else_branch.__str__()
        return f"({self.statement_type}" + "(" + self.condition.__str__() + ") " + self.then_branch.__str__()

class else_default_Statement(Node):
    condition: Node
    then_branch: Node

    # def __init__(self, condition: Node, then_branch: Node, else_branch: Node) -> None:
    def __init__(self,statement:TokenType, condition: Node, then_branch: Node) -> None:
        self.condition = condition
        self.then_branch = then_branch
        # self.else_branch = else_branch
        self.statement_type=""
        if statement==TokenType.tk_else:
            self.statement_type="else"
        elif statement==TokenType.tk_default:
            self.statement_type="elif"

    
    def __str__(self) -> str:
        #original
        #i commented it out because it is adding if statement even whene none are available
        # return "(if" + "(" + self.condition.__str__() + ")) " + self.then_branch.__str__() + " " + "else " + self.else_branch.__str__()
        return f"({self.statement_type}" + "(" + self.condition.__str__() + ") " + self.then_branch.__str__() 

class Indent(Node):
    def __init__(self,next: Node):
        self.next=next
    def __str__(self) -> str:
        return self.next.__str__()

class Dedent(Node):
    def __str__(self) -> str:
        return ")"