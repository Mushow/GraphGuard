# GraphGuard

GraphGuard is a deliberately vulnerable GraphQL API for managing user profiles. This project demonstrates common vulnerabilities in GraphQL APIs, provides key reproduction steps, and discusses mitigations to enhance security.

## Table of Contents
- [Setup Instructions](#setup-instructions)
- [API Endpoints](#api-endpoints)
- [Demonstrated Vulnerabilities](#demonstrated-vulnerabilities)
- [Security Measures](#security-measures)
- [Testing](#testing)
- [Project Structure](#project-structure)
- [Research and Documentation](#research-and-documentation)

## Setup Instructions

1. Clone the repository:
   `git clone https://github.com/Mushow/GraphGuard.git`
2. Navigate to the project directory: `cd GraphGuard`

2. Create a virtual environment and activate it:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   `pip install -r requirements.txt`

4. Initialize the database:
   `python -c "from database import init_db; init_db()"`

5. Run the application:
   `python app.py`

## API Endpoints

### Authentication
- POST /login: Generate JWT token.
  - Request:
    ```
    {
      "username": "admin",
      "password": "rootroot"
    }
    ```
  - Response:
    ```
    {
      "access_token": "your-generated-jwt-token"
    }
    ```

### GraphQL
- POST /graphql: Access GraphQL API (authentication required).

#### Example Queries and Mutations

- Query all user profiles:
  ```graphql
  query {
    allUsers {
      edges {
        node {
          id
          username
          email
          fullName
        }
      }
    }
  }
  ```

- Add a new user profile:
  ```graphql
  mutation {
    createUser(username: "johndoe", email: "john@example.com", fullName: "John Doe", password: "password123") {
      user {
        id
        username
      }
    }
  }
  ```

## Demonstrated Vulnerabilities

1. **SQL Injection**: Demonstrate how poorly constructed queries can lead to SQL injection.
2. **Broken Authentication**: Show how weak authentication mechanisms can be bypassed.
3. **Excessive Data Exposure**: Highlight how improper schema design can expose sensitive data.
4. **Inadequate Logging and Monitoring**: Demonstrate the lack of proper logging and monitoring.

## Security Measures

- **Input Validation**: Validate and sanitize inputs to prevent injection attacks.
- **JWT-based Authentication**: Secure API endpoints using JSON Web Tokens (JWT).
- **Proper Error Handling**: Avoid exposing sensitive information through error messages.
- **Rate Limiting**: Implement rate limiting to prevent abuse (future enhancement).
- **Comprehensive Logging and Monitoring**: Implement logging and monitoring to detect and respond to suspicious activities.

## Testing

- Use Postman to test API endpoints and verify functionality.
- Perform security testing using tools like OWASP ZAP and Burp Suite to identify and fix vulnerabilities.

## Project Structure

```
.
├── README.md
├── app.py
├── database.py
├── models.py
├── schema.py
├── security.py
├── requirements.txt
└── tests
    └── test_api.py
 ```

### Security Research

- **SQL Injection**: Examples and prevention techniques.
- **Broken Authentication**: How to strengthen authentication mechanisms.
- **Excessive Data Exposure**: Designing schemas to limit data exposure.
- **Inadequate Logging and Monitoring**: Implementing effective logging and monitoring solutions.
