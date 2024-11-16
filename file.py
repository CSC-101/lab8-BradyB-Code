import sys
from typing import Optional


# Task 2

def main():

    try:
        infile = open(sys.argv[1])
        file_contents1 = infile.readline()
        file_contents2 = infile.readline()
        float1: float = str2flt(file_contents1)
        float2: float = str2flt(file_contents2)
        print(float1, "+", float2, " = ", float1 + float2)
        infile.close()

    except FileNotFoundError:
        print("File not found")
        exit()

def str2flt(string: str)->Optional[float]:
    try:
        return float(string)
    except ValueError:
        return None



if __name__ == '__main__':
    main()


#Tests/Proof of Solution:
#Test 1
#C:\Users\BRBRO\AppData\Local\Programs\Python\Python312\python.exe "C:\Users\BRBRO\Downloads\CSC 101\lab8-BradyB-Code\file.py" txt_file.txt
#200.1 + 150.73  =  350.83
#
#Process finished with exit code 0
#
#
#Test 2
#C:\Users\BRBRO\AppData\Local\Programs\Python\Python312\python.exe "C:\Users\BRBRO\Downloads\CSC 101\lab8-BradyB-Code\file.py" txt_file_2.txt
#100.25 + 1.251  =  101.501
#
#Process finished with exit code 0
#
#
#Test 3
#C:\Users\BRBRO\AppData\Local\Programs\Python\Python312\python.exe "C:\Users\BRBRO\Downloads\CSC 101\lab8-BradyB-Code\file.py" fake_file.txt
#File not found
#
#Process finished with exit code 0
#
