import datetime


def write_log(user, msg):
    f = open(f'logs/{user}.log', 'a')
    f.write(f'{datetime.datetime.now()} {msg}\n')
    f.close()
