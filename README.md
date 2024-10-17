# Job Posting Web Scraper

This project is a Python-based web scraper designed to autonomously collect job postings from a specific webpage, including job title, description, duration, and posting date. The collected data is saved in either a text file or a CSV file(reset code according to your preference), with new data appended weekly to the same CSV file under a "new information" header. This project automates data collection, making it ideal for regular tracking and updating of job listings.

## Features
- **Automated Weekly Scraping**: Runs once a week without manual intervention.
- **Data Extraction**: Collects key information (job title, description, duration, and date posted).
- **Flexible Output**: Saves data to a CSV or text file, appending new information to a single CSV.
- **Scalable Design**: Easily adaptable to other websites with minor changes to the scraper configuration.

## Getting Started

### Prerequisites
- Python 3.x installed on your machine
- Required Python libraries: BeautifulSoup, Requests, Pandas (for CSV handling)

You can install the dependencies by running:
```bash
pip install -r requirements.txt
```

### Setup Instructions
1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/job-posting-web-scraper.git
   cd job-posting-web-scraper
   ```

2. **Add Target URL**: Open the script file and specify the webpage URL where job postings are located(and tweek code to your requirements). 

3. **Run the Scraper**: Run the script to perform the initial data collection.
   ```bash
   python your_script_name.py
   ```

4. **Automate Weekly Runs**: (Optional) Schedule the script to run weekly using cron (Linux/macOS) or Task Scheduler (Windows) to automate the data scraping.

## How to Test

If you would like to test this project:
1. **Run Script Manually**: Execute the Python script to collect the initial data from the target website. Confirm that a CSV file is created and that it contains the correct job information.
   ```bash
   python your_script_name.py
   ```

2. **Review File Output**: Check the CSV or text file to confirm that the data is correctly saved.

3. **Verify Weekly Automation**:
   - For quick testing, temporarily adjust the `time.sleep()` parameter in the script to a shorter duration.
   - Confirm that the program appends new data with each run under the "new information" header.
