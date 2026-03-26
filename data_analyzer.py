import logging
def analyze_data(data: list[dict], raw_lines, headers):
    verno = 0
    neverno = 0
    ocm = 0
    och = 0
    ocf = 0
    oce = 0
    kollm = 0
    kollh = 0
    kollf = 0
    kolle = 0
    kol = 0
    nesd = []
    all_correct = True
    excol = len(headers)
    srmat = 0
    srhis = 0
    srfil = 0
    sreco = 0
    for i, li in enumerate(raw_lines, 1):
        nowcol = li.strip().split(";")
        if nowcol[6] == "Не сдал":
            nesd += nowcol[1].split(",")
            logging.info(f"Студент {nowcol[1]} не сдал")
        if li != "":
            kol += li.count("Сдал")
        if len(nowcol) != excol:
            logging.warning(f"в строке {i} не корректное количество столбцов")
            all_correct = False
            continue
        else:
            logging.info(f"строка {i} корректна по количеству столбцов")
        try:
            student_id = int(nowcol[0])
            name = str(nowcol[1])
            group = str(nowcol[2])
            subject = str(nowcol[3])
            grade = int(nowcol[4])
            exam_date = str(nowcol[5])
            status = str(nowcol[6])
            if "Математика" in nowcol and li != "":
                ocm += grade
                kollm += 1
                if kollm > 0:
                    srmat = ocm / kollm
            elif "История" in nowcol and li != "":
                och += grade
                kollh += 1
                if kollh > 0:
                    srhis = och / kollh
            elif "Философия" in nowcol and li != "":
                ocf += grade
                kollf += 1
                if kollf > 0:
                    srfil = ocf / kollf
            elif "Экономика" in nowcol and li != "":
                oce += grade
                kolle += 1
                if kolle > 0:
                    sreco = oce / kolle
            if (student_id > 0 and
                    name.strip() != "" and
                    group.strip() != "" and
                    subject.strip() != "" and
                    2 <= grade <= 5 and
                    exam_date.strip() != "" and
                    status.strip() != ""):
                logging.info("строка заполнена верно")
                verno += 1
            else:
                logging.warning("в строке есть ошибки")
                neverno += 1
                all_correct = False
        except ValueError as e:
            logging.warning(f"ошибка в строке {i}: {e}")
            neverno += 1
            all_correct = False
        except IndexError as e:
            logging.warning(f"недостаточно данных в строке {i}: {e}")
            neverno += 1
            all_correct = False
        except Exception as e:
            logging.warning(f"непредвиденная ошибка в строке {i}: {e}")
            neverno += 1
            all_correct = False
    if all_correct:
        logging.info("все данные корректны")
    else:
        logging.warning("обнаружены ошибки в данных таблицы")
    print(f"Обработано строк: {verno + neverno}\nОшибочных строк: {neverno}\nКорректных строк: {verno}")
    print(f"Количество сдавших: {kol}")
    print("Среднее арифметическое по предметам:")
    if kollm > 0:
        print(f"  Математика: {srmat:.2f}")
    if kollh > 0:
        print(f"  История: {srhis:.2f}")
    if kollf > 0:
        print(f"  Философия: {srfil:.2f}")
    if kolle > 0:
        print(f"  Экономика: {sreco:.2f}")
    if nesd:
        print(f"Студенты, не сдавшие экзамены: {', '.join(nesd)}")
    else:
        print("Все студенты сдали экзамены")
    return all_correct, kol, srmat, srhis, srfil, sreco, nesd, verno, neverno