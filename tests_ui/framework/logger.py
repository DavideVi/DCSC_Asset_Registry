
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Logger():

    @staticmethod
    def log_head(message):
        print bcolors.HEADER + "== " + str(message) + " ==" + bcolors.ENDC

    @staticmethod
    def log_info(message):
        print bcolors.OKBLUE + "[INFO]\t" + bcolors.ENDC + str(message)

    @staticmethod
    def log_warn(message):
        print bcolors.WARNING + "[WARN]\t" + str(message) + bcolors.ENDC

    @staticmethod
    def log_fail(message):
        print bcolors.FAIL + "[FAIL]\t" + str(message) + bcolors.ENDC

    @staticmethod
    def log_blocked(message):
        print bcolors.FAIL + "[BLCK]\t" + str(message) + bcolors.ENDC

    @staticmethod
    def log_error(message):
        print bcolors.FAIL + "[ERRO]\t" + str(message) + bcolors.ENDC

    @staticmethod
    def log_success(message):
        print bcolors.OKGREEN + "[OK  ]\t" + bcolors.ENDC + str(message)

    @staticmethod
    def log_assert(logic_op, message):
        if (logic_op):
            log_success(message)
        else:
            log_fail(message)
