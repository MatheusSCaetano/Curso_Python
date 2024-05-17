
"""
x=5
def escopo():
    global x
    x=1
    
    def outra_funcao(y=10):
        print(y)


        def terceira_funcao(z=60):
            print(z)

        terceira_funcao()                            
    outra_funcao()
    print(x)


escopo()
print(x) 
"""

