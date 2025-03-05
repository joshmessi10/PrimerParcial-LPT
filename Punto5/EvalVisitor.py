import sys
from antlr4 import *
from LabeledExprLexer import LabeledExprLexer
from LabeledExprParser import LabeledExprParser
from LabeledExprVisitor import LabeledExprVisitor

class EvalVisitor(LabeledExprVisitor):
	def __init__(self):
		self.memory = {} #Diccionario para almacenar variables
	def visitAssign(self,ctx):
		id = ctx.ID().getText()
		value = self.visit(ctx.expr())
		if value is None:
			print('Error: asignacion vacia')
			return None
		self.memory[id] = value
		return value
	def visitPrintExpr(self, ctx):
		value = self.visit(ctx.expr())
		if value is not None:
			print(value)
		return value
	def visitReal(self,ctx):
		return float(ctx.REAL().getText())
	def visitComplex(self,ctx):
	    if ctx.COMPLEX().getText() == "i" or ctx.COMPLEX().getText() == "j" or ctx.COMPLEX().getText() == "I" or ctx.COMPLEX().getText() == "J":
	        complexVal = complex(0,1)
	    else:
	        complexVal = complex(0, float(ctx.REAL().getText()))    
	    return complexVal
	def visitImagine(self,ctx):
		return complex(float(ctx.REAL().getText()), ctx.COMPLEX().getText())
	
	

