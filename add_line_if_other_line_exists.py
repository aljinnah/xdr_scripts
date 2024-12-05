
from pathlib import Path

#file_path_str = 'H:/raw.txt'
file_path_str = 'C:/Windows/System32/drivers/etc/hosts'
file_path = Path(file_path_str)
with file_path.open(mode='a') as file:
    file.write(f'{'10.106.5.23 jxdgprod.bcbsms.com'}\n')

def modify_file(file_path, line_to_find, new_line):
    with file_path.open(mode='r') as file:
        lines = file.readlines()

    modified = False
    with file_path.open(mode='a') as file:
        for line in lines:
            if line.strip() == line_to_find.strip():
                file.write(f'{new_line}\n')
                modified = True
            else:
                file.write(line)

    return modified

if __name__ == '__main__':
    file_path_str = 'C:/Windows/System32/drivers/etc/hosts'
    file_path = Path(file_path_str)
    line_to_find = '10.106.5.23 jxdgprod.bcbsms.com'
    new_line = '10.106.5.23 jxdgprod.bcbsms.com'

    if modify_file(file_path, line_to_find, new_line):
        print('File modified successfully.')
    else:
        print('Line not found in the file.')