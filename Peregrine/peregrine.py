"""
*  
*  Copyright (c) Peregrine-lang, 2021. All rights reserved.
*
"""

import pe_parser
from lexer import lexer
print(lexer.lexer('    a=0\n    b=9\nc=5',"file"))