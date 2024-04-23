**README.md**

# Django Web Scraping App

This Django web application allows you to scrape product display names from provided URLs. It utilizes Python's BeautifulSoup library for web scraping and Django framework for web development.

## Features

- Scrapes product display names from specified URLs.
- Input URLs are declared  in views and display scraped product names.
- Supports running the app locally for development and testing purposes.

## Installation

1. Clone the repository to your local machine:

```
git clone https://github.com/ranjitgrewal/webscraper.git
```

2. Navigate to the project directory:

```
cd webscraper
```

3. Create a virtual environment (optional but recommended):

```
python3 -m venv venv
```

4. Activate the virtual environment:

```
# For Windows
venv\Scripts\activate

# For MacOS/Linux
source venv/bin/activate
```

5. Install dependencies:

```
pip install -r requirements.txt
```

## Usage

1. Run the Django development server:

```
python manage.py runserver
```

2. Open a web browser and go to http://localhost:8000/scrape to access the web application.

3. View the scraped product display names displayed on the web page in JSON format like below starting with URL and then the list of product.displayName

   {
     "https://shop.lululemon.com/c/womens-leggings/_/N-8r6?format=json":
       {"product.displayName":
         [
           ["Wunder Train High-Rise Tight 25\""],
            ["lululemon Align™ High-Rise Pant 28\""],
            ....
           ["Throwback Gather and Crow High-Rise Crop 21\""],
           ["Keep the Heat Thermal High-Rise Tight 28\" *Colourblock"]
         ]
      },
    "https://shop.lululemon.com/c/accessories/_/N-1z0xcmkZ1z0xl44Z8ok?format=json":
     {"product.displayName":
       [
         ["Team Canada Future Legacy Ball Cap *COC CPC Logo"],
         ["Classic Unisex Ball Cap *Wordmark"],
         ....
         ["Men's Fast and Free Running Hat"],
         ["Drawcord Hiking Cap"]
       ]
      }
   }

5. The cached content will be displayed for 15 minutes

## Testing

1. Run this command from the directory that has the manage.py to run unit test:

```
python3 manage.py test
```
