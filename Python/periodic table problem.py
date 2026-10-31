#periodic table problem
#subroutine to take property of element and output others

    def ElementInfo(Element):
        if Element == str('Li') or Element == str('Lithium'):
            return """Element: Lithium
Symbol: Li
Atomic Weight: 6.94
Group: Alkali Metals"""
        elif Element == str('Na') or Element == str('Sodium'):
            return """Element: Sodium
Symbol: Na
Atomic Weight 22.99
Group: Alkali Metals"""
        elif Element == str('K') or Element == str('Potassium'):
            return """Element: Potassium
Symbol: K
Atomic Weight: 39.1
Group: Alkali Metals"""
        elif Element == str('Br') or Element == str('Bromine'):
            return """Element: Bromine
Symbol: Br
Atomic Weight: 79.9
Group: Halogens"""
        elif Element == str('Cl') or Element == str('Chlorine'):
            return """Element: Chlorine
Symbol: Cl
Atomic Weight: 35.45
Group: Halogens"""
        elif Element == str('I') or Element == str('Iodine'):
            return """Element: Iodine
Symbol: I
Atomic Weight: 126.9
Group: Halogens"""
        
         
#main program
    print(ElementInfo(str(input("Element name/symbol:"))))

