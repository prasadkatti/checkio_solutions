
"""
Link to the problem statement
https://py.checkio.org/mission/brackets/
"""


def checkio(expression):

    BR_CHARS = u'[]{}()'
    OPEN_BR = u'({['
    CLOSE_BR = u')}]'

    matching_br = {}
    matching_br[u']'] = u'['
    matching_br[u')'] = u'('
    matching_br[u'}'] = u'{'

    stack = list()
    for char in expression:
        if char not in BR_CHARS:
            continue
        if char in OPEN_BR:
            stack.append(char)
        if char in CLOSE_BR:
            if not stack:
                return False
            if not stack[-1] == matching_br[char]:
                # print stack[-1], type(stack[-1])
                # print matching_br[char], type(matching_br[char])
                return False
            stack.pop()

    if stack:
        return False
    return True


assert checkio('((5+3)*2+1)') == True
assert checkio("{[(3+1)+2]+}") == True
assert checkio("(3+{1-1)}") == False
assert checkio("[1+1]+(2*2)-{3/3}") == True
assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False
assert checkio("2+3") == True





def checkio(expression):

    BR_CHARS = u'[]{}()'
    OPEN_BR = u'({['
    CLOSE_BR = u')}]'

    matching_br = {}
    matching_br[u']'] = u'['
    matching_br[u')'] = u'('
    matching_br[u'}'] = u'{'

    stack = list()
    for char in expression:
        if char not in BR_CHARS:
            continue
        if char in OPEN_BR:
            stack.append(char)
        if char in CLOSE_BR:
            if not stack:
                return False
            if not stack[-1] == matching_br[char]:
                # print stack[-1], type(stack[-1])
                # print matching_br[char], type(matching_br[char])
                return False
            stack.pop()

    if stack:
        return False
    return True


assert checkio('((5+3)*2+1)') == True
assert checkio("{[(3+1)+2]+}") == True
assert checkio("(3+{1-1)}") == False
assert checkio("[1+1]+(2*2)-{3/3}") == True
assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False
assert checkio("2+3") == True
