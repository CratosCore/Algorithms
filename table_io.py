import logging
def print_as_table(data: list[dict], headers: list[str]):
    for record in data:
        print(f"{record['Student ID']:<11}"
              f"{record['Name']:<20}"
              f"{record['Group']:<10}"
              f"{record['Subject']:<15}"
              f"{record['Grade']:<8}"
              f"{record['ExamDate']:<15}"
              f"{record['Status']:<10}")
def save_csv(filename: str, data: list[dict], headers: list[str], raw_lines):
    try:
        correct_lines = []
        excol = len(headers)
        correct_lines.append(raw_lines[0] if raw_lines else "")
        for i, li in enumerate(raw_lines[1:], 1):
            nowcol = li.strip().split(";")
            if len(nowcol) != excol:
                continue
            try:
                student_id = int(nowcol[0])
                name = nowcol[1].strip()
                group = nowcol[2].strip()
                subject = nowcol[3].strip()
                grade = int(nowcol[4])
                exam_date = nowcol[5].strip()
                status = nowcol[6].strip()
                if (student_id > 0 and
                        name != "" and
                        group != "" and
                        subject != "" and
                        2 <= grade <= 5 and
                        exam_date != "" and
                        status in ["Сдал", "Не сдал"]):
                    correct_lines.append(li)
            except (ValueError, IndexError):
                continue
        with open(filename, "w", encoding="utf-8") as pro:
            for line in correct_lines:
                if not line.endswith('\n'):
                    line = line + '\n'
                pro.write(line)
        logging.info(f"Сохранено в файл {filename}")
    except Exception as e:
        logging.error(f"Ошибка при сохранении файла {filename}: {e}")