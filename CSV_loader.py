import logging
def read_raw_lines(filename: str):
    headers = []
    raw_lines = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
        if not lines:
            return headers, raw_lines
        headers = lines[0].strip().split(";")
        print(f"{'Student ID':<11}{'Name':<20}{'Group':<10}{'Subject':<15}{'Grade':<8}{'ExamDate':<15}{'Status':<10}")
        for line in lines[1:]:
            stripped_line = line.strip()
            if stripped_line:
                raw_lines.append(stripped_line)
    except FileNotFoundError:
        logging.error(f"Ошибка: файл {filename} не найден")
    except Exception as e:
        logging.error(f"Ошибка при чтении файла: {e}")
    return headers, raw_lines