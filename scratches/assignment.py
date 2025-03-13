from typing import Optional
from pathlib import Path
import csv
from functools import singledispatch

# Regions
VALID_REGIONS = {"w": "West", "m": "Mountain", "c": "Central", "e": "East"}
# Sales date
DATE_FORMAT = "%Y-%m-%d"
MIN_YEAR, MAX_YEAR = 2000, 2_999
# files
FILEPATH = Path("C:/Users/ravir/AppData/Roaming/JetBrains/PyCharm2024.3/scratches")
ALL_SALES = FILEPATH / 'all_sales.csv'
ALL_SALES_COPY = FILEPATH / 'all_sales_copy.csv'
IMPORTED_FILES = FILEPATH / 'imported_files.txt'
NAMING_CONVENTION = "sales_qn_yyyy_r.csv"


def input_amount() -> float:
    while True:
        entry = float(input(f"{'Amount:':20}"))
        if entry > 0:
            return entry
        else:
            print(f"Amount must be greater than zero.")


def input_int(entry_item: str, high: int, low: int = 1, fmt_width: int = 20) -> int:
    prompt = f"{entry_item.capitalize()} ({low}-{high}):"
    while True:
        entry = int(input(f"{prompt:{fmt_width}}"))
        if low <= entry <= high:
            return entry
        else:
            print(f"{entry_item.capitalize()} must be between {low} and {high}.")


def input_year() -> int:
    return input_int('year', MAX_YEAR, MIN_YEAR)


def input_month() -> int:
    return input_int("month", 12, fmt_width=20)


def is_leap_year(year: int) -> bool:
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)


def cal_max_day(year: int, month: int) -> int:
    if is_leap_year(year) and month == 2:  # short-circuit
        return 29
    elif month == 2:
        return 28
    elif month in (4, 6, 9, 11):
        return 30
    else:
        return 31


def input_day(year: int, month: int) -> int:
    max_day = cal_max_day(year, month)
    parameters = {"entry_item": "day", "high": max_day}
    return input_int(**parameters)


def input_date() -> str:
    while True:
        entry = input(f"{'Date (yyyy-mm-dd):':20}").strip()
        if len(entry) == 10 and entry[4] == '-' and entry[7] == '-' \
                and entry[:4].isdigit() and entry[5:7].isdigit() \
                and entry[8:].isdigit():
            yyyy, mm, dd = int(entry[:4]), int(entry[5:7]), int(entry[8:])
            if (1 <= mm <= 12) and (1 <= dd <= cal_max_day(yyyy, mm)):
                if MIN_YEAR <= yyyy <= MAX_YEAR:
                    return entry
                else:
                    print(f"Year of the date must be between {MIN_YEAR} and {MAX_YEAR}.")
            else:
                print(f"{entry} is not in a valid date format.")
        else:
            print(f"{entry} is not in a valid date format.")


def input_region_code() -> Optional[str]:
    while True:
        fmt = 20
        valid_codes = tuple(VALID_REGIONS.keys())
        prompt = f"{f'Region {valid_codes}:':{fmt}}"
        code = input(prompt)
        if valid_codes.count(code) == 1:
            return code
        else:
            print(f"Region must be one of the following: {valid_codes}.")


def from_input1() -> dict:
    amount = input_amount()
    year = input_year()
    month = input_month()
    day = input_day(year, month)
    sales_date = f"{year}-{str(month).zfill(2)}-{day:02}"
    region_code = input_region_code()
    return {"amount": amount,
            "sales_date": sales_date,
            "region": region_code,
            }


def from_input2() -> dict:
    amount = input_amount()
    sales_date = input_date()
    region_code = input_region_code()
    return {"amount": amount,
            "sales_date": sales_date,
            "region": region_code,
            }


def is_valid_filename_format(filename: str) -> bool:
    if len(filename) == len(NAMING_CONVENTION) and \
            filename[:7] == NAMING_CONVENTION[:7] and \
            filename[8] == NAMING_CONVENTION[8] and \
            filename[13] == NAMING_CONVENTION[-6] and \
            filename[-4:] == NAMING_CONVENTION[-4:]:
        return True
    else:
        return False


def get_region_code(sales_filename: str) -> str:
    return sales_filename[sales_filename.rfind('.') - 1]


def already_imported(filepath_name: Path) -> bool:
    """Check if the file is already imported."""
    if not IMPORTED_FILES.exists():
        return False
    with open(IMPORTED_FILES, 'r') as file:
        return filepath_name.name in file.read().splitlines()


def add_imported_file(filepath_name: Path) -> None:
    """Add the filepath_name into IMPORTED_FILES"""
    with open(IMPORTED_FILES, 'a') as file:
        file.write(f"{filepath_name.name}\n")


@singledispatch
def import_sales(filepath_name: Path, delimiter: str = ',') -> list:
    with open(filepath_name, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=delimiter)
        filename = filepath_name.name
        region_code = filename[filename.rfind('.') - 1]
        imported_sales_list = []
        for amount_sales_date in reader:
            correct_data_types(amount_sales_date)
            amount, sales_date = amount_sales_date[0], amount_sales_date[1]
            data = {"amount": amount,
                    "sales_date": sales_date,
                    "region": region_code,
                    }
            imported_sales_list.append(data)
        return imported_sales_list  # within with statement


def cal_quarter(month: int) -> int:
    if month in (1, 2, 3):
        quarter = 1
    elif month in (4, 5, 6):
        quarter = 2
    elif month in (7, 8, 9):
        quarter = 3
    elif month in (10, 11, 12):
        quarter = 4
    else:
        quarter = 0
    return quarter


def get_region_name(region_code: str) -> str:
    return VALID_REGIONS[region_code]


def is_valid_region(region_code: str) -> bool:
    return tuple(VALID_REGIONS.keys()).count(region_code) == 1


def correct_data_types(row) -> None:
    """
    Try to convert valid amount to float type
    and mark invalid amount or sales date as '?'
    """
    try:  # amount
        row[0] = float(row[0])  # convert to float
    except ValueError:
        row[0] = "?"  # Mark invalid amount as bad
    # date
    if len(row[1]) == 10 and row[1][4] == '-' and row[1][7] == '-' \
            and row[1][:4].isdigit() and row[1][5:7].isdigit() and row[1][8:10].isdigit():
        yyyy, mm, dd = int(row[1][:4]), int(row[1][5:7]), int(row[1][8:10])
        if not (1 <= mm <= 12) or not (1 <= dd <= cal_max_day(yyyy, mm)):
            row[1] = "?"  # Mark invalid date as bad
    else:
        row[1] = "?"  # Mark invalid date as bad


def has_bad_amount(data: dict) -> bool:
    return data["amount"] == "?"


def has_bad_date(data: dict) -> bool:
    return data["sales_date"] == "?"


def has_bad_data(data: dict) -> bool:
    return has_bad_amount(data) or has_bad_date(data)


def view_sales(sales_list: list) -> bool:
    """
    Display "No sales to view" if there is no sales data in the sales_list.
    Otherwise, calculate the total amount and display sales data and the
    total amount on the console.
    """
    col1_w, col2_w, col3_w, col4_w, col5_w = 5, 15, 15, 15, 15  # column width
    bad_data_flag = False
    print(f"Sales list contains {len(sales_list)} items: {sales_list}")  # Debug print statement
    if len(sales_list) == 0:
        print("No sales to view.")
    else:
        total_w = col1_w + col2_w + col3_w + col4_w + col5_w
        print(f"{' ':{col1_w}}"
              f"{'Date':{col2_w}}"
              f"{'Quarter':{col3_w}}"
              f"{'Region':{col4_w}}"
              f"{'Amount':>{col5_w}}")
        print(horizontal_line := f"{'-' * total_w}")
        total = 0.0

        for idx, sales in enumerate(sales_list, start=1):
            if has_bad_data(sales):
                bad_data_flag = True
                num = f"{idx}.*"  # add period and asterisk
            else:
                num = f"{idx}."  # add period only

            amount = sales["amount"]
            if not has_bad_amount(sales):
                total += amount

            sales_date = sales["sales_date"]
            if has_bad_date(sales):
                bad_data_flag = True
                month = 0
            else:
                month = int(sales_date.split("-")[1])

            region = get_region_name(sales["region"])
            quarter = f"{cal_quarter(month)}"
            print(f"{num:<{col1_w}}"
                  f"{sales_date:{col2_w}}"
                  f"{quarter:<{col3_w}}"
                  f"{region:{col4_w}}"
                  f"{amount:>{col5_w}}")

        print(horizontal_line)
        print(f"{'TOTAL':{col1_w}}"
              f"{' ':{col2_w + col3_w + col4_w}}"
              f"{total:>{col5_w}}\n")
    return bad_data_flag


def add_sales1(sales_list: list) -> None:
    sales_list.append(data := from_input1())
    print(f"Sales for {data['sales_date']} is added.")


def add_sales2(sales_list: list) -> None:
    sales_list.append(data := from_input2())
    print(f"Sales for {data['sales_date']} is added.")


def initialize_content_of_files(delimiter: str = ',') -> None:
    """Copy the content of ALL_SALES_COPY to ALL_SALES.
    (ALL_SALES existing content will be overwritten by the content
    of ALL_SALES_COPY)
    Remove the content of IMPORTED_FILES.
    """
    # Clear all sales in ALL_SALES
    with open(ALL_SALES, 'w', newline='') as file:
        pass  # overwrite the file with nothing.
    with open(ALL_SALES_COPY, 'r') as input_file, \
            open(ALL_SALES, 'a', newline='') as output_file:
        csv_writer = csv.writer(output_file, delimiter=delimiter)
        for row in input_file:
            row = row.strip().split(',')
            correct_data_types(row)
            csv_writer.writerow(row)

    # Clear the IMPORTED_FILES
    with open(IMPORTED_FILES, 'w', newline='') as file:
        pass  # overwrite the file with nothing.


def main():
    sales_list = []
    while True:
        command = input("Enter command: ")
        if command == "add_sales1":
            add_sales1(sales_list)
        elif command == "add_sales2":
            add_sales2(sales_list)
        elif command == "view":
            view_sales(sales_list)
        elif command == "exit":
            break
        else:
            print("Unknown command.")


if __name__ == "__main__":
    main()
