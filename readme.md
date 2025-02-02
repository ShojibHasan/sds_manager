# Hotel Search and Booking Comparison Project

This is a Django-based web application that allows users to:
1. **Register/Login**
2. **Search for Hotels** based on city, price range, and star rating.
3. **View Search Results** and compare prices.
4. **Bookmark Favorite Hotels**

---
## Features
- **User Authentication:** Login & Register without email verification.
- **Hotel Search:** Filters by city, price range, and star rating.
- **Results Display:** Compares hotel prices across platforms.
- **Bookmarking:** Save hotels for later.
- **Web Scraping Support:** Uses Scrapy to fetch data from hotel booking sites.

---
## Technologies Used
- **Django** (Backend Framework)
- **PostgreSQL** (Database)
- **Scrapy & BeautifulSoup** (Web Scraping)
- **html / CSS** (Frontend Styling)

---
## Installation & Setup


### 1. Create a Virtual Environment
- Use python3.10
```sh
$ python3 -m venv venv
$ source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Clone project 
```sh
$ git clone git@github.com:ShojibHasan/sds_manager.git
```


### 3. create .env file and add database configuration as env.example

### 4. Install Dependencies
```sh
$ pip install -r requirements.txt
```
### 5. Apply Database Migrations
```sh
$ python manage.py migrate
```

### 6. Create a Superuser (Optional, for Admin Access)
```sh
$ python manage.py createsuperuser
```

### 7. Run the Development Server
```sh
$ python manage.py runserver
```
Access the site at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---
## Scraping Setup (Optional)
This project supports hotel data scraping using Scrapy.

### 1. Navigate to Scrapy Project Directory

### 2. Run Scraper to Fetch Hotel Data
```sh
$ scrapy crawl booking -o booking_data.json
$ scrapy crawl agoda -o agoda_data.json

```

### 3. Insert Data to Database
```sh
$ python manage.py import_hotels
```
---
## API Endpoints
| Endpoint         | Method | Description |
|-----------------|--------|-------------|
| `/`             | GET    | Home Page (Login / Register) |
| `/search/`      | GET    | Search for Hotels |
| `/results/`     | GET    | View Search Results |
| `/bookmark/`    | GET    | View Bookmarked Hotels |
| `/login/`       | POST   | User Login |
| `/register/`    | POST   | User Registration |
| `/logout/`      | POST   | User Logout |




