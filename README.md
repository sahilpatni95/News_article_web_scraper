# BBC_News_article_web_scraper

### Purpose ###
Create a solution that crawls for articles from a news website [BBC.com](https://www.bbc.com/), cleanses the response, stores in a mongo database.
### Solution ###
* Scrapy framework based crawler which traverses page links recursively and uses css response to fetch article details and text, then stores to external MongoDB server 

### Installation ###
* Download (or clone) the repo to your computer and unzip it.
* Ensure Python 3.x is installed: `python -V`
* Install required libraries: `pip install -r REQUIREMENTS.txt`
## Installation
 
 - You should have [**Python 3**](https://www.python.org/downloads/) installed in your computer.

#### Use the package manager [pip](https://pip.pypa.io/en/stable/) to install these required packages :

 - [PyMongo](https://api.mongodb.com/python/current/)  
```bash
pip install pymongo
```

## Usage
**Please make sure you have good internet connection** (to avoid speed issues).
- Run your terminal.
- Navigate (change directory) to the *BBC_News_article_web_scraper/NewsApp/* folder.
- Type the command :
```bash
scrapy crawl bbc
```
