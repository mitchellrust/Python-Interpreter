#!/usr/bin/env python
""" generated source for module EvalException """
#  (C) 2013 Jim Buffenbarger
#  All rights reserved.


class EvalException(Exception):
    """ generated source for class EvalException """

    def __init__(self, pos, msg):
        """ generated source for method __init__ """
        super(EvalException, self).__init__()
        self.pos = pos
        self.msg = msg

    def __str__(self):
        """ generated source for method toString """
        return "eval error" + ", pos=" + str(self.pos) + ", " + str(self.msg)