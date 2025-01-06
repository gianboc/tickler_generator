import os
import datetime
import argparse
import glob

def generate_daily_logs(year, end_month, end_day):
    """
    Generate daily log files for a given year.

    Args:
        year (int): The year for which daily log files are generated.
        end_month (int): The end month of the log generation period.
        end_day (int): The end day of the log generation period.
    """
    start_date = datetime.date(year, 1, 1)
    end_date = datetime.date(year, end_month, end_day)
    current_date = start_date

    # Remove all files in the "daily_logs" folder
    logs_folder = os.path.join(os.path.dirname(__file__), "daily_logs")
    if not os.path.exists(logs_folder):
        os.makedirs(logs_folder)
    for file_path in glob.glob(os.path.join(logs_folder, "*.md")):
        os.remove(file_path)

    while current_date <= end_date:
        week_number = current_date.isocalendar()[1]
        day_name = current_date.strftime("%A")
        month_abbrev = current_date.strftime("%b")
        month_name = current_date.strftime("%B")
        day_abbrev = current_date.strftime("%d")
        file_name = "Diary-"+current_date.strftime("%Y-%m-%d-Week") + str(week_number) + "-" + month_abbrev + day_abbrev + "-" + day_name
        file_path = os.path.join(logs_folder, file_name + ".md")
        with open(file_path, 'w') as file:
            file.write(f"# Daily Log for {current_date.strftime('%A, %B %d, %Y')}\n\n")
            file.write("## Waking up\n\n")
            file.write("## Morning\n\n")
            file.write("## Afternoon\n\n")
            file.write("## Evening\n\n")
            file.write("## Bedtime\n\n")
            file.write("## Exercise\n")
        current_date += datetime.timedelta(days=1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate daily log files for a given year.")
    parser.add_argument("input", help="Enter 'test' to run test function or a year to generate markdown files for that year")
    args = parser.parse_args()
    if args.input.lower() == 'test':
        year = 2025
        end_month = 2
        end_day = 28
    else:
        year = int(args.input)
        end_month = 12
        end_day = 31
        print(f"Generating logs for year: {year}, until: {end_month}/{end_day}")

    generate_daily_logs(year, end_month, end_day)