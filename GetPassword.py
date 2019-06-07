import argparse
import getpass


class Password:

    DEFAULT = 'Prompt if not specified'

    def __init__(self, value):
        if value == self.DEFAULT:
            value = getpass.getpass('Server Password: ')
        self.value = value

    def __str__(self):
        return self.value

def main(PrintBoolean,FromFileBoolean):
    if FromFileBoolean:
        from cryptography.fernet import Fernet
        filep = open('/home/MonitoringEXOTools/pass', 'rb')
        password = filep.read()
        filep.close()
        filek = open('/home/MonitoringEXOTools/key.key', 'rb')
        key = filek.read()
        filek.close()
        f = Fernet(key)
        decrypted = f.decrypt(password)
        parser = argparse.ArgumentParser(
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        parser.add_argument('-u', '--username', help='Specify username',
                            default=getpass.getuser())
        parser.add_argument('-p', '--password', type=Password, help='Specify password',
                            default=decrypted)
        args = parser.parse_args()
    else:
        parser = argparse.ArgumentParser(
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        parser.add_argument('-u', '--username', help='Specify username',
                            default=getpass.getuser())
        parser.add_argument('-p', '--password', type=Password, help='Specify password',
                            default=Password.DEFAULT)
        args = parser.parse_args()

    return args

    if PrintBoolean: print(args.username, args.password)

if __name__ == "__main__":
    main(True)
