[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/zN2AskmG)
# XKCD Comic Viewer

This web application uses the XKCD API to display comics dynamically. Users can view the latest comic, navigate between comics using Previous and Next buttons, and search for specific comics by entering a comic number. The application demonstrates API integration, JSON parsing, input validation, and error handling using Flask.

---

## Features Implemented

- [X] Feature #1: Display the Latest Comic
- [X] Feature #2: Display a Specific Comic by Number
- [X] Feature #4: Navigation (Previous/Next)
- [X] Feature #5: Search by Comic Number Form

---

## Technologies Used

- Python 3.8+
- Flask 3.0.0
- Requests 2.31.0
- XKCD Public API

---

## Installation and Setup

### Prerequisites
- Python 3.8 or higher
- pip installed

### Steps to Run

1. Clone or download this repository

2. Navigate to the project directory in your terminal:
   ```
   cd projectName
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the application:
   ```
   python app.py
   ```

5. Open your web browser and go to:
   ```
   http://localhost:5000
   ```

## Usage
- The homepage displays the latest XKCD comic.
- Click **Previous** to view the prior comic.
- Click **Next** to move forward (disabled on the latest comic).
- Use the search box to enter a comic number (e.g., 614).
- Invalid inputs (letters, negative numbers, 0, or non-existent comics) display a friendly error message.

---

## Screenshots
<img width="1906" height="959" alt="Screenshot 2026-02-17 213046" src="https://github.com/user-attachments/assets/11f52bf3-b58b-4d1a-98c1-673381bc7311" />
<img width="1919" height="884" alt="Screenshot 2026-02-17 213035" src="https://github.com/user-attachments/assets/5f9eea07-5910-422b-90f6-f06652f53b9c" />
<img width="1919" height="889" alt="Screenshot 2026-02-17 213058" src="https://github.com/user-attachments/assets/969458ba-4dc1-4650-bad7-a6de407cea8f" />

Example:
```
![Latest Comic View](screenshots/latest-comic.png)
![Search Feature](screenshots/search.png)
```

## API Endpoints Used

- `GET /info.0.json` — Fetches the most recent comic.
- `GET /{comic_number}/info.0.json` — Fetches a specific comic by number.

---

## Challenges and Solutions

- One challenge was handling invalid user input, such as entering "0" or non-numeric values. Initially, this caused the application to crash. I resolved this by validating input using type checking and conditional logic before making the API request.

- Another challenge was managing API errors, such as requesting a comic number that does not exist. The XKCD API returns a 404 error for missing comics, so I implemented error handling using `try/except` blocks and status code checks to display user-friendly messages instead of crashing the application.

- Through this assignment, I learned how to make HTTP requests using the `requests` library, parse JSON responses into Python dictionaries, and dynamically render API data within a Flask web application.

---


## Future Improvements

If I had more time, I would add:
- A Random Comic button
- Improved UI styling
- A page that displays multiple recent comics in a grid layout

---
## Author

Najwa Aissaoui
