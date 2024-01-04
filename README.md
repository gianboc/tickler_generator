# Code Description
This tool automates the creation of digital Tickler Files in Markdown format. By generating a file for each day, it serves as a virtual 'folder' where users can store notes, tasks, or reminders specific to that date. The automated system ensures that you have a dedicated space for all your upcoming commitments, enabling efficient tracking and management of future tasks and information.

## What is a "Tickler" File?
A Tickler File, as conceptualized in the GTD (Getting Things Done) methodology by David Allen, is a future-oriented system designed to remind you of tasks or information on a specific date. Traditionally comprising 43 folders for each day of the month and each month of the year, this system helps in keeping track of upcoming commitments. It ensures that nothing falls through the cracks by bringing items to your attention at the right time. Our digital version in Markdown format replicates this functionality, aiding in personal organization and productivity.

## Usage

1. Clone the repository to your local machine using `git clone https://github.com/gianboc/tickler_generator`.

2. Navigate to the cloned repository using `cd tickler_generator`.

3. Run the script with the desired year or 'test' as an argument. For example:
    - To generate markdown files for the year 2024, use `python3 generate.py 2024`.
    - To run the test function, use `python3 generate.py test`. This will execute it only up to the end of February

4. The script will generate a markdown file for each day of the specified year, or run the test function, depending on the argument provided. Each generated markdown file is named with the format `YYYY-MM-DD-WeekWW-D.md`, where `YYYY` is the year, `MM` is the month, `DD` is the day, `WeekWW` is the week number (like "Week1", "Week2", "Week17", etc.), and `D` is the day of the week. For example, a file for March 3, 2024, which falls on the 9th week and is a Sunday, would be named `2024-03-03-Week9-Sunday.md`. These files are saved in the "ticklers" folder.

