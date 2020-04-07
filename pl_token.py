#!/usr/bin/env python
""" generated source for module Token """
#  (C) 2013 Jim Buffenbarger
#  All rights reserved.


class Token(object):
    """ generated source for class Token """

    def __init__(self, token, lexeme=None):
        """ generated source for method __init__ """
        if lexeme is None:
            lexeme = token
        self.token = token
        self.lexeme = lexeme

    def tok(self):
        """ generated source for method tok """
        return self.token

    def lex(self):
        """ generated source for method lex """
        return self.lexeme

    def __eq__(self, t):
        """ generated source for method equals """
        if t is None:
            return False
        return self.token == t.token

    def __str__(self):
        """ generated source for method toString """
        return "<" + str(self.tok()) + "," + str(self.lex()) + ">"
