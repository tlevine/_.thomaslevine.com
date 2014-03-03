def seq(messages, start = 0, end = None):
    keys = list(reversed(sorted(messages.keys())))[start:end]
    return [messages[k] for k in keys]

def page(messages, n, step = 10):
    return seq(messages, step * n, step * (n + 1))
