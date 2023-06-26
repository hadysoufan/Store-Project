# Store Shop 🚀

This is a ReactJs, Django and PostgresSQL Project

## Table of Contents

- [Store Shop 🌀](#store-shop-)
  - [Table of Contents](#table-of-contents)
  - [Description](#description)
  - [Installation 🔽](#installation-)
  - [Usage](#usage)
  - [Endpoints](#endpoints)
  - [Contributing](#contributing)

## Description

This project includes code snippets for user authentication, registration, profile management, and user management in a web application. It provides the necessary backend functionality for user-related operations.


## Installation 🔽

To run this project locally, follow these steps:

1. Clone the repository: `git clone (https://github.com/hadysoufan/Store-Project.git)`

2. Install the required dependencies: Run the following command to install the necessary packages: `npm install react-bootstrap boostwatch react-router-dom react-router-bootstrap`

3. For Python dependencies, create a virtual environment and install the required packages using pip: 
`
virtualenv env
source env/bin/activate
pip install django django-admin django-restframework axios pillow redux react-redux redux-thunk redux-devtools-extension djangorestframework-simplejwt
`
4. Configure the project settings according to your environment.
5. Run the development server: `<to be build>`


## Usage

Once the project is set up and the server is running, you can perform various user-related operations using the provided endpoints.

## Endpoints

1. **Register User**

   - **Endpoint:** `/api/register/`
   - **Method:** POST
   - **Description:** Register a new user.
   - **Parameters:**
     - `name`: The user's name.
     - `email`: The user's email.
     - `password`: The user's password.
   - **Returns:** The registered user's information.

2. **User Login**

   - **Endpoint:** `/api/login/`
   - **Method:** POST
   - **Description:** Authenticate a user and generate an access token.
   - **Parameters:**
     - `email`: The user's email.
     - `password`: The user's password.
   - **Returns:** An access token for the authenticated user.

3. **Get User Profile**

   - **Endpoint:** `/api/profile/`
   - **Method:** GET
   - **Description:** Retrieve the profile information of the authenticated user.
   - **Authentication:** Bearer Token
   - **Returns:** The profile information of the authenticated user.

4. **Update User Profile**

   - **Endpoint:** `/api/profile/`
   - **Method:** PUT
   - **Description:** Update the profile information of the authenticated user.
   - **Authentication:** Bearer Token
   - **Parameters:**
     - `name`: The updated name.
     - `email`: The updated email.
     - `password`: The updated password.
   - **Returns:** The updated profile information of the user.

5. **Get All Users** (Admin Only)

   - **Endpoint:** `/api/users/`
   - **Method:** GET
   - **Description:** Retrieve the information of all users (admin access required).
   - **Authentication:** Bearer Token (Admin Access)
   - **Returns:** The information of all users.

## Contributing

Contributions to this project are welcome! If you find any issues or would like to suggest improvements, please create a new issue or submit a pull request.
