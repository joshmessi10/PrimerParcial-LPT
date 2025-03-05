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
	def visitId(self, ctx):
		id = ctx.ID().getText()
		return self.memory.get(id, None)
	def visitMulDiv(self, ctx):
		left = self.visit(ctx.expr(0))
		right = self.visit(ctx.expr(1))
		if ctx.op.type == LabeledExprParser.MUL:
			return left * right
		else:
			if right == 0:
				print("Error: Division por cero")
				return None
			else:
				return left / right
	def visitAddSub(self,ctx):
		left = self.visit(ctx.expr(0))
		right = self.visit(ctx.expr(1))
		if right == LabeledExprParser.COMPLEX:
		    return complex(left, right)
		if ctx.op.type == LabeledExprParser.ADD:
			return round(left + right, 10)
		return round(left - right, 10)
	def visitParens(self, ctx):
	    text = ctx.getText()
	    if not (text.startswith("(") and text.endswith(")")):
	        print("Error: Parentesis no cerrados correctamente")
	        return None
	    return self.visit(ctx.expr())
	def visitNeg(self,ctx):
		value = self.visit(ctx.expr())
		return -value if value is not None else None
	def visitPos(self,ctx):
	    value = self.visit(ctx.expr())
	    return value if value is not None else None
	
	

