class BaseArg(object):

    def __init__(self):
        self.gpio = 1

    def validate(self):
         if self.gpio == 0:
            raise Exception("You have to choice a gpio value for pin.")

    def get_argument(self, argv, i):
        arg_splited = argv[i].split("=")
        
        if i != 0 and len(arg_splited) != 2:
            raise Exception("Invalid argument ", arg_splited)
        
        arg = arg_splited[0]
        val = arg_splited[1]
        return arg, val
    