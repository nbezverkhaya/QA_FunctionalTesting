# Demo QA Functional Testing

This project is designed to demonstrate functional testing using Selenium WebDriver, Python, and Pytest. It includes page objects, test cases, and utility modules.

## Project Structure

- `pages/`: Contains the Page Object classes for the website's various pages.
  - `base_page.py`: Base page class with common methods.
  - `home_page.py`: Page object for the home page.
  - `registration_page.py`: Page object for the registration page.
  - `search_page.py`: Page object for the search functionality.

- `tests/`: Contains test cases for functional testing.
  - `test_home_page.py`: Tests for the home page.
  - `test_registration.py`: Tests for registration functionality.
  - `test_search_functionality.py`: Tests for search functionality.
  - `data_for_testing.py`: Sample test data.

- `utils/`: Contains utility modules.
  - `driver.py`: Sets up and configures the Selenium WebDriver.
  - `config.py`: Configuration settings (e.g., URLs).

- `.venv/`: Virtual environment for dependencies.

## Installation and Setup

1. **Clone the repository:**
```bash
   git clone https://github.com/nbezverkhaya/DemoQAFunctionalTesting.git
```
2. **Navigate to the project directory:**
```bash
   cd demo-qa-functional-testing
```
3. **Create a virtual environment and activate it:**
```bash
python3 -m venv .venv
source .venv/bin/activate
 ```
4. **Install the dependencies:**
```bash
pip install -r requirements.txt
```

## Running the Tests
1. **Run all tests:**
```
pytest
```
2. **Run a specific test file:**
```
pytest tests/test_home_page.py
```
## Dependencies
All dependencies are listed in the requirements.txt file. Notable libraries:

* selenium
* pytest
* webdriver-manager

## Contributing
Feel free to fork the repository and submit pull requests. Contributions are always welcome!

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE.txt) file for details.