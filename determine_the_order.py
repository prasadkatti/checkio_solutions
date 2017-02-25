
"""
Link to the problem statement
https://py.checkio.org/mission/determine-the-order/
"""

MAX_WORD_LEN = 10


def remove_node(dag):
    """ Remove node with least number of outgoing edges """

    min_out_degree = MAX_WORD_LEN + 1
    terminal_nodes = []
    for k, v in dag.items():
        if len(v) < min_out_degree:
            min_out_degree = len(v)
            terminal_nodes = [k]
        elif len(v) == min_out_degree:
            terminal_nodes.append(k)
    removed_node = sorted(terminal_nodes).pop()
    for v in dag.values():
        if removed_node in v:
            v.remove(removed_node)
    dag.pop(removed_node)
    return removed_node


def checkio(words):

    # Build a set of all symbols
    symbols = set()
    for w in words:
        symbols.update(w)

    # Construct a Directed Acyclic Graph (DAG)
    # For each key(symbol), the value is a list of all symbols
    # that come immediately after it in any of the words.
    dag = {}
    for s in symbols:
        dag[s] = []
    for w in words:
        for i in xrange(len(w) - 1):
            x, y = w[i], w[i+1]
            if x != y and y not in dag[x]:
                dag[x].append(y)

    order = []
    while len(order) != len(symbols):
        order.append(remove_node(dag))

    return ''.join(reversed(order))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(["acb", "bd", "zwa"]) == "zwacbd", \
        "Just concatenate it"
    assert checkio(["klm", "kadl", "lsm"]) == "kadlsm", \
        "Paste in"
    assert checkio(["a", "b", "c"]) == "abc", \
        "Cant determine the order - use english alphabet"
    assert checkio(["aazzss"]) == "azs", \
        "Each symbol only once"
    assert checkio(["dfg", "frt", "tyg"]) == "dfrtyg", \
        "Concatenate and paste in"
