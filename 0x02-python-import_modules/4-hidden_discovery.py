#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4.pyc
    for i in dir(hidden_4.pyc):
        if not i.startswith('__'):
            print("{}".format(i))
    
