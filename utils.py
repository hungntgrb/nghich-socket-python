def isClosed(socket_):
    return '[closed]' in str(socket_)


ENCODING = 'utf-8'
HEADER = 20  # "16            "
DISCONNECT_MSG = '!D'
ABORTED_MSG = '!ABORTED'
ACCEPTED_MSG = 'CONNECTION ACCEPTED'
