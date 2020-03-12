# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import io
from datetime import datetime

#p
def Rating_timestamp(in_file_path):
    source = io.open(in_file_path, mode="r", encoding="utf-8")
    content = source.readlines()
    output = open("./latest/converted" + in_file_path[8:-4] + "_out.txt", mode="w+",encoding="utf-8")
    
    for line in content:
        line_elements = line.split("::")
        output.write("^".join(line_elements[0:3] + [datetime.fromtimestamp(int(line_elements[3])).strftime("%d/%m/%Y")]) + '\n')
        
        
    output.close()
    source.close()
        
Rating_timestamp("./latest/ratings.dat")
