# Blog Website

Welcome to the Blog Website repository! This project is a full-featured blog platform built using HTML, CSS, JavaScript, jQuery, Bootstrap, and Django as the backend framework. The website allows users to read, create, and manage blog posts with a modern and responsive design.

## Table of Contents

-   [Features](#features)
-   [Technologies Used](#technologies-used)
-   [Installation](#installation)
-   [Usage](#usage)
-   [Contributing](#contributing)
-   [License](#license)

## Features

-   **Responsive Design**: The website is fully responsive and works on various devices and screen sizes.
-   **User Authentication**: Users can register, log in, and manage their profiles.
-   **Create & Manage Posts**: Authenticated users can create, edit, and delete their blog posts.
-   **Search Functionality**: Users can search for blog posts by keywords.
-   **Category Filtering**: Posts can be filtered by categories.
-   **Rich Text Editor**: A rich text editor is provided for writing blog posts.

## Technologies Used

-   **Frontend**:
    
    -   HTML
    -   CSS
    -   JavaScript
    -   jQuery
    -   Bootstrap
-   **Backend**:
    
    -   Django
    -   SQLite (default)

## Installation

Follow these steps to set up the project locally:

### Prerequisites

-   Python 3.x
-   pip (Python package installer)
-   virtualenv (optional but recommended)

### Clone the Repository

bash

Copy code

`git clone https://github.com/JIVAN-SUBEDI/Blog..git`
`cd blog.` 

### Set Up the Virtual Environment

It is recommended to use a virtual environment to manage dependencies.

bash

Copy code

``python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate` `` 

### Install Dependencies

`pip install -r requirements.txt` 

### Apply Migrations

`python manage.py migrate` 

### Create a Superuser

`python manage.py createsuperuser` 

### Run the Development Server

`python manage.py runserver` 

Open your web browser and go to `http://127.0.0.1:8000` to see the website in action.

## Usage

-   **Home Page**: View recent blog posts.
-   **Post Details**: Click on a post title to read the full post and see comments.
-   **User Authentication**: Register or log in to create and manage posts.
-   **Create Post**: Use the rich text editor to write new blog posts.
-   **Edit/Delete Post**: Edit or delete your own posts.
-   **Search and Filter**: Use the search bar and category filters to find specific posts.

## Contributing

We welcome contributions to enhance this project. If you want to contribute, please follow these steps:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/your-feature-name`).
3.  Make your changes.
4.  Commit your changes (`git commit -m 'Add some feature'`).
5.  Push to the branch (`git push origin feature/your-feature-name`).
6.  Open a pull request.

Please make sure your code adheres to our coding standards and includes relevant tests.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

----------

Thank you for visiting the Blog Website repository! If you have any questions or need further assistance, feel free to contact us or open an issue. Happy coding!