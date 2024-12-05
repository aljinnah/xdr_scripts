from pathlib import Path

def modify_file(file_path, new_line):
    """
    Modify a file if a certain line does not exist within the file
    Args:
        file_path: Path of the file that will be modified
        new_line: Line that will be added if it is not already within he file
    Returns:
        True if file is modified oir False if not.
    Author:
        Mohammad Abu Al Jinnah 
    """
    with file_path.open(mode='r') as file:
        lines = file.read().splitlines()
    #    print("All the lines:{}".format(lines))
    #    print("This is new_line: {}".format(new_line))

    modified = False
    if new_line not in lines:
        with file_path.open(mode='a') as file:
            file.write(f'\n{new_line}\n')
            modified = True
    return modified
    

if __name__ == '__main__':
    file_path_str = 'C:/Windows/System32/drivers/etc/hosts'
    #file_path_str = 'h:/raw.txt'
    file_path = Path(file_path_str)
    raw_line = '10.106.5.23 jxdgprod.bcbsms.com'
    new_line=raw_line.strip()

    if modify_file(file_path, new_line):
        print('File modified successfully.')
    else:
        print('Line already in the file')