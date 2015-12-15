import re

# Taken from Jay Conrod's IMP interpreter tutorial
# http://jayconrod.com/posts/38/a-simple-interpreter-from-scratch-in-python-part-2

class Lexer:
    # Define in subclasses
    TOKEN_MAPPINGS = []

    def __init__(self, characters):
        self.characters = characters

    def __lex(self, characters, token_exprs):
        pos = 0
        tokens = []
        while pos < len(characters):
            match = None
            for token_expr in token_exprs:
                pattern, tag = token_expr
                regex = re.compile(pattern, re.IGNORECASE)
                match = regex.match(characters, pos)
                if match:
                    text = match.group(0)
                    if tag:
                        token = (text, tag)
                        tokens.append(token)
                    break
            if not match:
                raise SyntaxError('Illegal character: %s\\n' % characters[pos])
            else:
                pos = match.end(0)
        return tokens

    def lex(self):
        return self.__lex(self.characters, self.TOKEN_MAPPINGS)
