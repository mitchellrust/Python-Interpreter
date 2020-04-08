#!/usr/bin/env python
""" generated source for module Environment """
#  (C) 2013 Jim Buffenbarger
#  All rights reserved.
from pl_evalexception import EvalException


class Environment(object):
    """ generated source for class Environment """

    def __init__(self):
        """ generated source for method __init__ """
        self.map = {}
        self.funcMap = {}
        
    def putFunc(self, var, val):
        self.funcMap[var] = val
        return val
        
    def getFunc(self, pos, var):
        if var in self.funcMap:
            return self.funcMap[var]
        raise EvalException(pos, "undefined function: " + var)

    def put(self, var, val):
        """ generated source for method put """
        self.map[var] = val
        return val

    def get(self, pos, var):
        """ generated source for method get """
        if var in self.map:
            return self.map[var]
        raise EvalException(pos, "undefined variable: " + var)
