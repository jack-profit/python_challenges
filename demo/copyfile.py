#!/usr/bin/env python3

import sys

def copy_file(income,outgo):
    '''
    # di yi zhong
    with open(income) as infile:
        with open(outgo,'w') as outfile:
            for k, v in enumerate(infile.readlines()):
                outfile.write(str(k+1))
                outfile.write(v)
    '''
    # di er zhong
    with open(income) as infile, open(outgo, 'w') as outfile:
        for k, v in enumerate(infile.readlines()):
            outfile.write(str(k + 1))
            outfile.write(v)

if __name__ == '__main__':
    if len(sys.argv) == 3:
        copy_file(sys.argv[1],sys.argv[2])

        pass
        with open(sys.argv[2]) as resultfile:
            print(resultfile.readlines())
    else:
        raise 'Paramters Error'

    
