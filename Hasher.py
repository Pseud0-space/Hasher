from hashlib import sha256, sha512, sha224, sha384, md5
from colorama import init
import sys
import os

arguments = sys.argv

init()

class bcolors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[31m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    BGRED = '\033[41m'
    WHITE = '\033[37m'


def help():
    data = """\nHasher [OPTION] [WORK]\n
    [OPTIONS]:
    \t-F, --func :- to speciffy the hashing function to use
    \t-H, --hash :- to speciffy the Data to be hashed
            
    [WORK]:
    \tsha512 :- hashing function to use ==> sha512
    \tsha384 :- hashing function to use ==> sha384
    \tsha256 :- hashing function to use ==> sha256
    \tsha224 :- hashing function to use ==> sha224
    \tmd5    :- hashing function to use ==> MD5
            
    \t"sample text" :- Text to be hashed

    """
    print(data)

if len(arguments) == 1:
    dat = """\nHasher [OPTION]\n
[OPTION] :
    -h , --help :- for help\n"""
    print(dat)
    sys.exit()    


if "--func" in arguments:
    num = arguments.index("--func") 

if "-F" in arguments:
    num = arguments.index("-F")

if "--hash" in arguments: 
    num0 = arguments.index("--hash")
    data = arguments[num0 + 1]

if "-H" in arguments:
    num0 = arguments.index("-H")
    data = arguments[num0 + 1]


if "-h" in arguments:
    num1 = arguments.index("-h")
    if arguments[num1] == "-h":
        help()
        sys.exit()

if "--help" in arguments:
    num1 = arguments.index("--help")
    if arguments[num1] == "--help":
        help()
        sys.exit()
     

try:
    os.system("clear")

    if arguments[num] == "-F" or arguments[num] == "--func":
        logo = """
         _   _           _               
        | | | | __ _ ___| |__   ___ _ __ 
        | |_| |/ _` / __| '_ \ / _ \ '__|
        |  _  | (_| \__ \ | | |  __/ |   
        |_| |_|\__,_|___/_| |_|\___|_|   

            ~~| By:- Pseudo |~~          """

        print(bcolors.RED + bcolors.BOLD)
        print(logo)
        print(bcolors.ENDC)

        if arguments[num + 1] == "sha256":
            if arguments[num0] == "-H"or arguments[num0] == "--hash":
                data = data.encode()
                hashed = sha256(data).hexdigest()
                
                print(f"\n{bcolors.GREEN +'[*] Hashing function used'+ bcolors.ENDC} ==> {bcolors.YELLOW +arguments[num + 1]+ bcolors.ENDC}")
                print(f"{bcolors.GREEN +'[*] Data to be Hashed'+ bcolors.ENDC} ==> {bcolors.YELLOW +arguments[num0 + 1]+ bcolors.ENDC}")

                print(f"\n{bcolors.BLUE +'[HASH] -->'+ bcolors.ENDC}\n\n{hashed}\n")

            else:
                help()

        elif arguments[num + 1] == "sha512":
            if arguments[num0] == "-H"or arguments[num0] == "--hash":
                data = data.encode()
                hashed = sha512(data).hexdigest()

                print(f"\n{bcolors.GREEN +'[*] Hashing function used'+ bcolors.ENDC} ==> {bcolors.YELLOW +arguments[num + 1]+ bcolors.ENDC}")
                print(f"{bcolors.GREEN +'[*] Data to be Hashed'+ bcolors.ENDC} ==> {bcolors.YELLOW +arguments[num0 + 1]+ bcolors.ENDC}")

                print(f"\n{bcolors.BLUE +'[HASH] -->'+ bcolors.ENDC}\n\n{hashed}\n")

            else:
                help()

        elif arguments[num + 1] == "sha224":
            if arguments[num0] == "-H"or arguments[num0] == "--hash":
                data = data.encode()
                hashed = sha224(data).hexdigest()

                print(f"\n{bcolors.GREEN +'[*] Hashing function used'+ bcolors.ENDC} ==> {bcolors.YELLOW +arguments[num + 1]+ bcolors.ENDC}")
                print(f"{bcolors.GREEN +'[*] Data to be Hashed'+ bcolors.ENDC} ==> {bcolors.YELLOW +arguments[num0 + 1]+ bcolors.ENDC}")

                print(f"\n{bcolors.BLUE +'[HASH] -->'+ bcolors.ENDC}\n\n{hashed}\n")

            else:
                help()

        elif arguments[num + 1] == "sha384":
            if arguments[num0] == "-H"or arguments[num0] == "--hash":
                data = data.encode()
                hashed = sha384(data).hexdigest()

                print(f"\n{bcolors.GREEN +'[*] Hashing function used'+ bcolors.ENDC} ==> {bcolors.YELLOW +arguments[num + 1]+ bcolors.ENDC}")
                print(f"{bcolors.GREEN +'[*] Data to be Hashed'+ bcolors.ENDC} ==> {bcolors.YELLOW +arguments[num0 + 1]+ bcolors.ENDC}")

                print(f"\n{bcolors.BLUE +'[HASH] -->'+ bcolors.ENDC}\n\n{hashed}\n")

            else:
                help()

        elif arguments[num + 1] == "md5":
            if arguments[num0] == "-H"or arguments[num0] == "--hash":
                data = data.encode()
                hashed = md5(data).hexdigest()

                print(f"\n{bcolors.GREEN +'[*] Hashing function used'+ bcolors.ENDC} ==> {bcolors.YELLOW +arguments[num + 1]+ bcolors.ENDC}")
                print(f"{bcolors.GREEN +'[*] Data to be Hashed'+ bcolors.ENDC} ==> {bcolors.YELLOW +arguments[num0 + 1]+ bcolors.ENDC}")

                print(f"\n{bcolors.BLUE +'[HASH] -->'+ bcolors.ENDC}\n\n{hashed}\n")

            else:
                help()



    else:
        dat = """\nHasher [OPTION]\n
    [OPTION] :
        -h , --help :- for help\n"""
        print(dat)
        sys.exit()

except Exception:
    dat = """\nHasher [OPTION]\n
[OPTION] :
    -h , --help :- for help\n"""
    print(dat)
    sys.exit()
