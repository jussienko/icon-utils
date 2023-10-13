import os
from glob import glob
import sys
import re

# acc_pat = re.compile(r'!\$ACC.*PARALLEL.*REDUCTION.*VECTOR')
acc_pat = re.compile(r'!\$ACC.*PARALLEL.*REDUCTION')
procedure_start = re.compile(r'(^ *SUBROUTINE|^ *FUNCTION)')
procedure_end = re.compile(r'(^ *END SUBROUTINE|^ *END FUNCTION)')


#for path, subdirs, files in os.walk('.'):
if True:
    if len(sys.argv) > 1:
        files = sys.argv[1:]
    else: 
        files = glob("*/*f90")

    path = '.'
    for file in files:
        if file.endswith(".f90") or file.endswith(".F90"):
            filename = os.path.join(path, file)
            with open(filename.strip(), 'r') as f:
                vec_reduction = False
                within_acc_region = False
                subroutine = ''
                acc_directive = ''
                linenumber = 1
                for line in f:
                    if procedure_end.search(line):
                        # empty routine name
                        subroutine = ''
                    if procedure_start.search(line):
                        subroutine = line.split()[1].split('(')[0]
                    # Build up ACC directive and when complete check pattern
                    # if '!$ACC PARALLEL' in line:
                    if acc_pat.search(line):
                        acc_directive += line.strip()
                        within_acc_region = True
                    if within_acc_region and ('VECTOR' in line):
                        print(filename, subroutine, linenumber)
                    if '!$ACC END PARALLEL' in line:
                        within_acc_region = False
                    # elif acc_directive:
                    #    if acc_pat.search(acc_directive):
                    #        print(filename, subroutine, linenumber)
                        # empty directive
                        acc_directive = ''
                    linenumber += 1

