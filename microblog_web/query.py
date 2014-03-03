def seq(messages, start = 0, end = None):
    return reversed(sorted(messages))[start:end]

def page(messages, n, step = 10):
    return seq(messages, step * n, step * (n + 1))
