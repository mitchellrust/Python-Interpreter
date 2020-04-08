#!/usr/bin/env python
from pl_environment import Environment


class Function(object):
    def __init__(self, param_id, expr):
        self.param_id = param_id
        self.expr = expr
        self.env = Environment()
    
    def call(self, param):
        self.env.put(self.param_id, param)
        return self.expr.eval(self.env)