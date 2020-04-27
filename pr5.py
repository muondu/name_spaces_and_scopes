def foo():
    i_am_non_local = 5
    
    def bleep():
        i_am_non_local = 10
    
    def oof():
        nonlocal i_am_non_local
        i_am_non_local = 20
        
    def bop():
        global i_am_non_local
        i_am_non_local = 30
    
    bleep()
    print('After bleep:', i_am_non_local)
    oof()
    print('After oof:', i_am_non_local)
    bop()
    print('After bop:', i_am_non_local
    
foo()
print('Globally:', i_am_non_local)
        