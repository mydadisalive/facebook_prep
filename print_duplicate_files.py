#!/usr/bin/python3

import sys
import os
import stat
from collections import defaultdict
import subprocess 
import hashlib
from functools import partial


def usage():
    ''' print usage '''
    print("Usage: "+sys.argv[0]+" <dir_name>")


def walktree(root_dir):
    for root_dir_file,_,files in os.walk(root_dir, topdown=False, followlinks=True):
        for filename in files:
            file_full_path = os.path.join(root_dir_file, filename)
            file_mode = os.stat(file_full_path).st_mode
            if not stat.S_ISREG(file_mode):
                continue
            file_dev = os.stat(file_full_path).st_dev
            if file_dev != os.stat(root_dir).st_dev:
                continue

            file_md5 = md5sum(file_full_path)
            md5_to_file_table[file_md5] += [file_full_path]


    for md5, duplicate_candidates_list in md5_to_file_table.items():
        if len(duplicate_candidates_list) > 1:
            for i in range(0, len(duplicate_candidates_list)):
                for j in range(i+1, len(duplicate_candidates_list)):
                    cand_i = duplicate_candidates_list[i]
                    cand_j = duplicate_candidates_list[j]
                    cand_i_inode = os.stat(cand_i).st_ino
                    cand_j_inode = os.stat(cand_j).st_ino
                    cand_i_size = os.stat(cand_i).st_size
                    cand_j_size = os.stat(cand_j).st_size
                    if cand_i_inode == cand_j_inode:
                        continue
                    if cand_i_size != cand_j_size:
                        continue
                    if cand_i_size < 100:
                        continue
                    ret_val = subprocess.call(["diff", "-b", cand_i, cand_j])
                    if ret_val == 0:
                        print("found duplicates ", cand_i, cand_j)
                    else:
                        print("found two files with same md5s that are different!!!")

    #for key in sorted(md5_to_file_table):
    #    val = md5_to_file_table[key]
    #    if len(val) > 1:
    #        print(key,val)

def md5sum(file_full_path):
    with(open(file_full_path, mode='rb')) as f:
        bytes = f.read()
        return hashlib.md5(bytes).hexdigest()


# MAIN
if __name__ == '__main__':
    if len(sys.argv) != 2 or not os.path.isdir(sys.argv[1]):
        usage()
        sys.exit(1)

    root_dir = sys.argv[1]
    md5_to_file_table = defaultdict(list)
    walktree(root_dir)
