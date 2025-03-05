# Programa en ANTLR

```
export CLASSPATH=".:/usr/loca/lib/antlr-4.13.2-complete.jar:$CLASSPATH"
alias antlr4='java -Xmx500M -cp "/usr/local/lib/antlr-4.13.2-complete.jar:$CLASSPATH" org.antlr.v4.Tool'
alias grun='java org.antlr.v4.gui.TestRig'
```

```
antlr4 -no-listener -visitor Trigo.g4
javac TrigoCalc.java Trigo*.java
java TrigoCalc expr.in
```

```
antlr4 -Dlanguage=Python3 -visitor Trigo.g4
python3 TrigoCalc.py
```
