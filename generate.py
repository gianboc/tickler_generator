import os
# Usage:
#     This script generates tickler files for a given year. To run the script, use the following command:
#     python generate.py <year>
#     Replace <year> with the desired year for which you want to generate tickler files. For example:
#     python generate.py 2024
#     Alternatively, you can run the script in test mode by passing 'test' as the argument:
#     python generate.py test
#     In test mode, the script will generate tickler files for the period from January 1, 2024, to February 28, 2024.

import datetime
import argparse
import glob

def generate_ticklers(year, end_month, end_day):
    """
    Generate tickler files for a given year.

    Args:
        year (int): The year for which tickler files are generated.
        end_month (int): The end month of the tickler generation period.
        end_day (int): The end day of the tickler generation period.
    """
    start_date = datetime.date(year, 1, 1)
    end_date = datetime.date(year, end_month, end_day)
    current_date = start_date

    # Remove all files in the "ticklers" folder
    ticklers_folder = os.path.join(os.path.dirname(__file__), "ticklers")
    for file_path in glob.glob(os.path.join(ticklers_folder, "*.md")):
        os.remove(file_path)

    while current_date <= end_date:
        week_number = current_date.isocalendar()[1]
        day_name = current_date.strftime("%A")
        month_abbrev = current_date.strftime("%b")
        month_name = current_date.strftime("%B")
        day_abbrev = current_date.strftime("%d")
        file_name = current_date.strftime("%Y-%m-%d-Week") + str(week_number) + "-" + month_abbrev + day_abbrev + "-" + day_name
        file_path = os.path.join(ticklers_folder, file_name + ".md")

        with open(file_path, "w") as file:
            file.write(f"Good morning! Today is {day_name}, {month_name} {day_abbrev}\n\n")
        print(file_path)

        current_date += datetime.timedelta(days=1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Enter 'test' to run test function or a year to generate markdown files for that year")
    args = parser.parse_args()

    if args.input.lower() == 'test':
        year = 2024
        end_month = 2
        end_day = 28
    else:
        year = int(args.input)
        end_month = 12
        end_day = 31

    generate_ticklers(year, end_month, end_day)
