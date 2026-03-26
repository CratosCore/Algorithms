from table_io import save_csv, print_as_table
from data_validator import*
from data_analyzer import*
from CSV_loader import*
import logging
logging.basicConfig(
    level=logging. INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log", encoding='utf-8'),
        logging.StreamHandler()
    ]
)
def main():
    logging.info("Запуск обработки данных")
    headers, raw_lines = read_raw_lines("data.CSV")
    valid_data = []
    for line in raw_lines:
        record = validate_row_structure(line, headers)
        if not record:
            continue
        converted_record, error = convert_row_types(record)
        if error:
            logging.warning("Ошибка преобразования типов данных")
            continue
        if not validate_semantic(converted_record):
            logging.warning("Ошибка семантики")
            continue
        valid_data.append(converted_record)
    print_as_table(valid_data, headers)
    all_correct, kol, srmat, srhis, srfil, sreco, nesd, verno, neverno = analyze_data(
        valid_data, raw_lines, headers
    )
    save_csv("processed_data.csv", valid_data, headers, raw_lines)


if __name__ == "__main__":
    main()
#условие необходимо, чтобы выполнялась только основная функция "main", иначе при запуске программы все файлы начнут выполняться по отдельности