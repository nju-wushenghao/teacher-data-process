from write import write
from read import read
from time import sleep

if __name__ == '__main__':
    read_file_name = input("Enter input file name: (default: input.xlsx)")
    if read_file_name == "":
        read_file_name = "input.xlsx"

    read_res = read(read_file_name)
    print("Read from excel: ")
    print(read_res)

    write_file_name = input("Enter output file name: (default: output.xlsx)")
    if write_file_name == "":
        write_file_name = "output.xlsx"

    write_res = write(write_file_name, read_res)
    print("write_res:")
    print(write_res)

    # sleep(20)