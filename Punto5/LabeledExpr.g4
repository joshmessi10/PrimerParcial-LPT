grammar LabeledExpr;

prog : stat+;

stat: expr NEWLINE	        # printExpr
	| ID '=' expr NEWLINE   # assign
	| NEWLINE		# blank
	;

expr: '(' expr ')'	# Parens
	| '-' expr	# Neg
	| '+' expr #Pos
	| expr op=('*' | '/') expr #MulDiv
	| expr op=('+' | '-') expr #AddSub
	| REAL op=('+' | '-') COMPLEX #Imagine
	| REAL #Real
	| COMPLEX #Complex
	| ID #Id
	;

MUL : '*';
DIV : '/';
ADD : '+';
SUB : '-';
ID : [a-zA-Z]+ ;
REAL : [0-9]+ ('.' [0-9]*)? ;
COMPLEX : ([0-9]+ ('.' [0-9]*)?)? [iIjJ];
NEWLINE : 'r'? '\n';
WS :  [ \t]+ -> skip ;
