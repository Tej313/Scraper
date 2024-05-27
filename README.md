# Scraper Project

This project contains a web scraper that fetches job listings, extracts skill phrases, and saves the top skills into a JSON file.

## Structure

- `Scraper/`
  - `__init__.py`: Initializes the Scraper package.
  - `beautiful_soup.py`: Contains the main scraping and data extraction logic.
  - `helpers.py`: Contains helper functions used in the project.
- `tests/`
  - `scraper_tests.py`: Contains tests for the `beautiful_soup.py` script.
  - `helpers_tests.py`: Contains tests for the `helpers.py` script.
- `.gitignore`: Specifies files and directories to be ignored by git.
- `LICENSE`: The license under which the project is distributed.
- `README.md`: This file.
- `requirements.txt`: Lists the dependencies required to run the project.
- `setup.py`: Script for setting up the project as a package.

## Setup

1. Clone the repository.
2. Create a virtual environment and activate it.
3. Install dependencies using `pip install -r requirements.txt`.
4. Run the script using `python Scraper/beautiful_soup.py`.
5. Run tests using `python -m unittest discover tests`.

## License

This project is licensed under the MIT License - see the LICENSE file for details..
