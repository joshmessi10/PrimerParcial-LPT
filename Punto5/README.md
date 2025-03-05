# Programa en ANTLR para el calculo de numeros complejos

```
export CLASSPATH=".:/usr/loca/lib/antlr-4.13.2-complete.jar:$CLASSPATH"
alias antlr4='java -Xmx500M -cp "/usr/local/lib/antlr-4.13.2-complete.jar:$CLASSPATH" org.antlr.v4.Tool'
alias grun='java org.antlr.v4.gui.TestRig'
```


```
antlr4 -Dlanguage=Python3 -visitor LabeledExpr.g4
python3 Calc.py
```
