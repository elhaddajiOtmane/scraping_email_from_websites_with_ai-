# Web Scraping with Google Gemini and ScrapeGraphAI

This project uses Google's Gemini AI model in conjunction with [ScrapeGraphAI](https://github.com/ScrapeGraphAI/Scrapegraph-ai) to perform web scraping tasks, specifically extracting phone numbers and email addresses from websites.

## About ScrapeGraphAI

This project heavily relies on [ScrapeGraphAI](https://github.com/ScrapeGraphAI/Scrapegraph-ai), an innovative tool that combines web scraping with AI-powered analysis. ScrapeGraphAI allows for efficient and intelligent extraction of information from web pages, which we've integrated with Google's Gemini model for enhanced processing.

## Prerequisites

- Python 3.7 or higher
- A Google API key for accessing the Gemini model
- ScrapeGraphAI library and its dependencies

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/elhaddajiotmane/scraping_email_from_websites_with_ai.git
   cd scraping_email_from_websites_with_ai
   ```

2. Create a virtual environment:
   ```
   python -m venv gemini-env
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     gemini-env\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source gemini-env/bin/activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Configuration

1. Create a `.env` file in the project root directory.
2. Add your Google API key to the `.env` file:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

## Usage

To run the web scraping script:

```
python main.py
```

This will use ScrapeGraphAI to scrape the specified website (default is https://example.com/) and extract phone numbers and email addresses, with processing enhanced by the Gemini model.

## Project Structure

- `main.py`: The main script that performs the web scraping using ScrapeGraphAI and Gemini.
- `requirements.txt`: List of Python package dependencies, including ScrapeGraphAI.
- `.env`: Configuration file for environment variables (not tracked in git).
- `README.md`: This file, containing project documentation.

## Generating Requirements

To generate or update the `requirements.txt` file based on your current environment:

```
python generate_specific_requirements.py
```

This will create a `requirements.txt` file with the specific packages used in this project, including ScrapeGraphAI and its dependencies.

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [ScrapeGraphAI](https://github.com/ScrapeGraphAI/Scrapegraph-ai) for providing the core web scraping and AI integration functionality
- Google for providing the Gemini AI model
- The creators and maintainers of the libraries used in this project