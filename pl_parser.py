#!/usr/bin/env python

from pl_syntaxexception import SyntaxException
from pl_node import *
from pl_scanner import Scanner
from pl_token import Token


class Parser(object):
    """ generated source for class Parser """
    def __init__(self):
        self.scanner = None

    def match(self, s):
        """ generated source for method match """
        self.scanner.match(Token(s))

    def curr(self):
        """ generated source for method curr """
        return self.scanner.curr()

    def pos(self):
        """ generated source for method pos """
        return self.scanner.position()

    def parseMulop(self):
        """ generated source for method parseMulop """
        if self.curr() == Token("*"):
            self.match("*")
            return NodeMulop(self.pos(), "*")
        if self.curr() == Token("/"):
            self.match("/")
            return NodeMulop(self.pos(), "/")
        return None

    def parseAddop(self):
        """ generated source for method parseAddop """
        if self.curr() == Token("+"):
            self.match("+")
            return NodeAddop(self.pos(), "+")
        if self.curr() == Token("-"):
            self.match("-")
            return NodeAddop(self.pos(), "-")
        return None
        
    def parseRelop(self):
        if self.curr() == Token("<"):
            self.match("<")
            return NodeRelop(self.pos(), "<")
        if self.curr() == Token("<="):
            self.match("<=")
            return NodeRelop(self.pos(), "<=")
        if self.curr() == Token(">"):
            self.match(">")
            return NodeRelop(self.pos(), ">")
        if self.curr() == Token(">="):
            self.match(">=")
            return NodeRelop(self.pos(), ">=")
        if self.curr() == Token("<>"):
            self.match("<>")
            return NodeRelop(self.pos(), "<>")
        if self.curr() == Token("=="):
            self.match("==")
            return NodeRelop(self.pos(), "==")
        return None

    def parseFact(self):
        """ generated source for method parseFact """
        if self.curr() == Token("("):
            self.match("(")
            expr = self.parseExpr()
            self.match(")")
            return NodeFactExpr(expr)
        if self.curr() == Token("-"):
            self.match("-")
            fact = self.parseFact()
            return NodeFactFact(fact)
        if self.curr() == Token("id"):
            id = self.curr()
            self.match("id")
            if self.curr() == Token("("):
                self.match("(")
                expr = self.parseExpr()
                self.match(")")
                return NodeFuncCall(id.lex(), expr)
            else:
                return NodeFactId(self.pos(), id.lex())
        num = self.curr()
        self.match("num")
        return NodeFactNum(num.lex())

    def parseTerm(self):
        """ generated source for method parseTerm """
        fact = self.parseFact()
        mulop = self.parseMulop()
        if mulop is None:
            return NodeTerm(fact, None, None)
        term = self.parseTerm()
        term.append(NodeTerm(fact, mulop, None))
        return term

    def parseExpr(self):
        """ generated source for method parseExpr """
        term = self.parseTerm()
        addop = self.parseAddop()
        if addop is None:
            return NodeExpr(term, None, None)
        expr = self.parseExpr()
        expr.append(NodeExpr(term, addop, None))
        return expr
        
    def parseBoolExpr(self):
        expr_1 = self.parseExpr()
        relop = self.parseRelop()
        expr_2 = self.parseExpr()
        bool_expr = NodeBoolExpr(expr_1, relop, expr_2)
        return bool_expr

    def parseAssn(self):
        """ generated source for method parseAssn """
        id = self.curr()
        self.match("id")
        self.match("=")
        expr = self.parseExpr()
        assn = NodeAssn(id.lex(), expr)
        return assn

    def parseWr(self):
        """ generated source for method parseWr """
        self.match("wr")
        expr = self.parseExpr()
        wr = NodeWr(expr)
        return wr
        
    def parseRd(self):
        self.match("rd")
        id = self.curr()
        self.match("id")
        num = input()
        rd = NodeRd(id.lex(), float(num))
        return rd
        
    def parseIf(self):
        self.match("if")
        bool_expr = self.parseBoolExpr()
        self.match("then")
        stmt = self.parseStmt()
        sub_stmt = None
        if self.curr() == Token("else"):
            self.match("else")
            sub_stmt = self.parseStmt()
        if_stmt = NodeIf(bool_expr, stmt, sub_stmt)
        return if_stmt
        
    def parseWhile(self):
        self.match("while")
        bool_expr = self.parseBoolExpr()
        self.match("do")
        stmt = self.parseStmt()
        while_stmt = NodeWhile(bool_expr, stmt)
        return while_stmt
        
    def parseBegin(self):
        self.match("begin")
        block = self.parseBlock()
        self.match("end")
        begin = NodeBegin(block)
        return begin
        
    def parseFuncDecl(self):
        self.match("def")
        id = self.curr()
        self.match("id")
        self.match("(")
        param_id = self.curr()
        self.match("id")
        self.match(")")
        self.match("=")
        expr = self.parseExpr()
        func_decl = NodeFuncDecl(id.lex(), param_id.lex(), expr)
        return func_decl

    def parseStmt(self):
        """ generated source for method parseStmt """
        if self.curr() == Token("rd"):
            rd = self.parseRd()
            return NodeStmt(rd)
        if self.curr() == Token("wr"):
            wr = self.parseWr()
            return NodeStmt(wr)
        if self.curr() == Token("if"):
            if_stmt = self.parseIf()
            return NodeStmt(if_stmt)
        if self.curr() == Token("while"):
            while_stmt = self.parseWhile()
            return NodeStmt(while_stmt)
        if self.curr() == Token("begin"):
            begin = self.parseBegin()
            return NodeStmt(begin)
        if self.curr() == Token("def"):
            func_decl = self.parseFuncDecl()
            return NodeStmt(func_decl)
        if self.curr() == Token("id"):
            assn = self.parseAssn()
            return NodeStmt(assn)
        return None

    def parseBlock(self):
        """ generated source for method parseBlock """
        stmt = self.parseStmt()
        rest = None
        if self.curr() == Token(";"):
            self.match(";")
            rest = self.parseBlock()
        block = NodeBlock(stmt, rest)
        return block
        
    def parseProg(self):
        block = self.parseBlock()
        return NodeProg(block)

    def parse(self, program):
        """ generated source for method parse """
        self.scanner = Scanner(program)
        self.scanner.next()
        return self.parseProg()
