#!/usr/bin/env python
""" generated source for module SyntaxException """
#  (C) 2013 Jim Buffenbarger
#  All rights reserved.


class SyntaxException(Exception):
    """ generated source for class SyntaxException """

    def __init__(self, pos, expected, found):
        """ generated source for method __init__ """
        super(SyntaxException, self).__init__()
        self.pos = pos
        self.expected = expected
        self.found = found

    def __str__(self):
        """ generated source for method toString """
        return "syntax error" + ", pos=" + str(self.pos) + ", expected=" + str(self.expected) + ", found=" + str(self.found)