from pathlib import Path
#file_path_str = 'H:/raw.txt'
file_path_str = 'C:/Windows/System32/drivers/etc/hosts'
file_path = Path(file_path_str)
with file_path.open(mode='a') as file:
    file.write(f'\n{'x.x.x.x hostname.domain.com'}\n')