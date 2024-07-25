import argparse

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

    args = parser.parse_args()
    print(args.scount, args.top, args.dt)

    if args.scount:
        print(f"-s => {args.scount}")
    elif args.top:
        print(f"-t => {args.top}")
        if args.dt:
            print(f"-d => {args.dt}")
        else:
            print("to-do")
    else:
        parser.print_help()
