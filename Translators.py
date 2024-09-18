# Simple Translators 
# pip install translators==5.3.1
import translators as ts
txt = input('txt : ')
res = ts.google(txt , to_language='fa')
print (res)