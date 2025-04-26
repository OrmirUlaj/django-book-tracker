# Book Tracker System for interview part-2

This is the Django-based web application developed for the technical challenge given to me.  
It allows authenticated users to scrape book data, manage their own book lists, and perform CRUD operations.


## Setup Instructions 

1. Clone the repository:

    ```
    git clone https://github.com/OrmirUlaj/django-book-tracker.git
    cd django-book-tracker
    ```

2. Create and activate a virtual environment:

    ```
    python -m venv venv
    venv\Scripts\activate   # Windows
    source venv/bin/activate  # Mac/Linux
    ```

3. Install required packages:

    ```
    pip install -r requirements.txt
    ```

4. Apply migrations:

    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Create a superuser:

    ```
    python manage.py createsuperuser
    ```

6. Run the development server:

    ```
    python manage.py runserver
    ```

7. Visit in your browser:

    ```
    http://127.0.0.1:8000/
    ```


## Project Structure and Logic

The project is organized into two main Django apps:

- **book_tracker/**: Contains the project-wide settings, configurations, and URLs.
- **books/**: The main application handling all functionality related to users, books, scraping, and views.

### Key Components:

- **models.py**:
  Defines the `Book` model, including fields like title, price, stock, description, UPC, and number of reviews.
  Each Book is linked to a specific user (the owner).

- **forms.py**:
  Contains a `BookForm` (ModelForm) for adding and editing books manually through the web interface.

- **views.py**:
  Handles all user interactions including:
  - Listing books
  - Adding a book
  - Editing a book
  - Deleting a book
  - Triggering web scraping manually
  Access to these views is protected by login requirements.

- **urls.py**:
  Maps URL routes to their respective views for registration, login, logout, books management, and scraping.

- **templates/books/**:
  Contains all HTML templates for rendering the frontend, styled with Bootstrap.

- **scraper.py**:
  Contains the web scraping logic using Selenium, allowing users to scrape book information from https://books.toscrape.com according to their assigned pages.
  Superusers can scrape all available pages.

- **admin.py**:
  Registers the `Book` model in Django Admin for easy management during development and testing.

---

### Application Flow:

1. Users register or login.
2. Logged-in users are directed to the Book List page.
3. Users can:
   - Scrape books manually based on their assigned pages.
   - Add new books manually.
   - Edit or delete books they own.
4. Admins (superusers) have full access to all books and users' data.
5. Session-based authentication ensures secure access to user-specific content.
6. CSRF protection is enabled for all forms and scraping actions.

## Bonus Features

- Admin-only Dashboard added
  - Shows Total Books in System
  - Shows Total Manually Added Books
  - Shows Your Own Books
  - Lists Top Contributors


### Made by Ormir Ulaj