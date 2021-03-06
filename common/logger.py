import os

def six_digit(x):
    x = str(x)
    return '0' * (6 - len(x)) + x

class Logger:
    def __init__(self, cfg):
        self.cfg = cfg
        self.path = os.path.join(cfg.result_path, 'logs')
        os.makedirs(self.path)

    def log_epoch(self, data):
        f = open(os.path.join(self.path, f"epoch_{six_digit(data['epoch'])}.log"), 'w')
        f.write(f"{','.join([str(x) for x in data.keys() if x != 'epoch'])} {','.join([str(v) for k, v in data.items() if k != 'epoch'])}")
        f.close()