import logging
def validate_row_structure(line: str, headers: list[str]):
    polya = line.split(";")
    if len(polya) != len(headers):
        return None
    for pole in polya:
        if not pole.strip():
            return None
    record = {}
    for i in range(len(headers)):
        record[headers[i]] = polya[i].strip()
    return record
def convert_row_types(record: dict):
    try:
        converted_record = record.copy()
        if "Student ID" in converted_record:
            converted_record["Student ID"] = int(converted_record["Student ID"])
        if "Grade" in converted_record:
            converted_record["Grade"] = int(converted_record["Grade"])
        return converted_record, None
    except ValueError as e:
        return record, logging.warning(f"Ошибка преобразования типов: {e}")
    except Exception as e:
        return record, logging.warning(f"Непредвиденная ошибка: {e}")
def validate_semantic(record: dict):
    try:
        student_id = record.get("Student ID")
        if not isinstance(student_id, int) or student_id <= 0:
            return False
        grade = record.get("Grade")
        if not isinstance(grade, int) or grade < 2 or grade > 5:
            return False
        status = record.get("Status", "")
        if status not in {"Сдал", "Не сдал"}:
            return False
        required_fields = ["Name", "Group", "Subject", "ExamDate"]
        for field in required_fields:
            value = record.get(field, "")
            if not value or not isinstance(value, str):
                return False
        exam_date = record.get("ExamDate", "")
        if not exam_date or len(exam_date) < 8:
            return False
        return True
    except Exception:
        return False