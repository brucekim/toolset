import sys
import os
import subprocess
import getopt

def helpdoc():
    print("Usage:")
    print("%s -vh -i inputfile" % sys.argv[0])
    print("")
    print("-v : Scanning results in verbose")
    print("-h : shows usages")
    print("-i inputfile: inputfile describes scanning targets such as ip address, port lists")
    print("example of file_port_info.txt")
    print("")
    print("inputfile format")
    print("target_name, ip_addr, port1, port2, ...")
    print("Ports can be given in range, xx-yy")
    print("server#1, 192.168.0.2, 8080, 80, 8443, 443, 22")
    print("server#3, 192.168.0.4, 8443, 443, 22, 10000-10010")

# tools for scanning port
# nc: nc -zvw3 target port
# nmap: nc -sS -p port target
def handle(infile, verbose):
    lists = []
    options = ""
    if verbose==True:
        options = "-zvw3"
    else:
        options = "-zw3"

    with open(infile) as f:
        for line in f:
            if not line.startswith("#"):
                a_list = [elements.strip() for elements in line.split(',')]
                lists.append(a_list)

    for a_list in lists:
        target_name = a_list[0]
        target_ip = a_list[1]
        port_list = a_list[2:]
        print("Scanning... %s(%s)" % (target_name, target_ip))
        for target_port in port_list:
            #print("Scanning %s(%s), port %s ..." % (target_name, target_ip, target_port))
            subprocess.run(["nc", "-zvw3", target_ip, target_port])


if __name__ == "__main__":
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hvi:")
    except getopt.GetoptError as err:
        print(err)
        helpdoc()
        sys.exit(2)
    verbose = False
    infile = None
    for o, a in opts:
        if o == "-v":
            verbose = True
        elif o == "-h":
            helpdoc()
            sys.exit()
        elif o == "-i":
            infile = a
        else:
            assert False, "unhandled options"

    if (infile != None):
        handle(infile, verbose)
