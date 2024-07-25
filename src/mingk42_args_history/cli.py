import argparse
from mingk42_args_history.db.utils import count, top, pretty


hello_msg=lambda :"hello"

def cmd():
    msg=hello_msg()
    print(msg)

    parser = argparse.ArgumentParser(
                    prog='ProgramName',
                    description='What the program does',
                    epilog='Text at the bottom of help')
    #parser.add_argument('filename')                                # positional argument
    parser.add_argument('-s', '--scount')                                # positional argument
    #parser.add_argument('-c', '--count')                           # option that takes a value
    parser.add_argument('-t', '--top')                           # option that takes a value
    #parser.add_argument('-v', '--verbose', action='store_true')    # on/off flag  --> true/false 
    parser.add_argument('-d', '--dt')    # on/off flag  --> true/false
    parser.add_argument('-p', '--pretty', action="store_true")

    args = parser.parse_args()
    print("********* input data **********")
    print("query","top","dt",sep="\t")
    print(args.scount, args.top, args.dt,sep="\t")
    print("*******************************")

    if args.scount:
        print(f"-s => {args.scount}",end="\n\n")
        print(count(args.scount))
    elif args.top:
        print(f"-t => {args.top}",end="\n\n")
        if args.dt:
            print(f"-d => {args.dt}",end="\n\n")
            if args.pretty:
               print(pretty(args.dt, int(args.top)))
            else:
               print(top(args.dt, int(args.top)))
        else:
            parser.error("-t 옵션은 -d와 함께 사용되어야 합니다.")
    else:
        parser.print_help()
