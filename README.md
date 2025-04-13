# Python App to connet to a Databse MySQL

## Installation
**
1. Clone the repository:
    ```sh
    git clone https://github.com/josefloressv/flask_mysql_db_app.git
    cd flask_mysql_db_app
    ```

2. Create and activate a virtual environment:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Running the Application
1. Run a MySQL Database in Docker
   ```sh
   docker run --name mysql-container -e MYSQL_ROOT_PASSWORD= -e MYSQL_DATABASE=testdb -p 3306:3306 -d mysql:latest
   # Check database logs
   docker logs mysql-container
   ```
2. Set Environment Variables
   ```sh
   export DB_HOST=127.0.0.1
   export DB_USER=root
   export DB_PASSWORD=
   ```
3. Start the Flask application:
    ```sh
    python app.py
    ```

4. The application will be running at `http://127.0.0.1:5000/`.

## Accessing the API Documentation

You can access the Swagger UI for API documentation at: http://127.0.0.1:5000/apidocs/



## API Endpoints

### `GET /`

A simple endpoint to connect to the database.

**Parameters:**
as environment variables
- `name` (query, string, optional): The name of the person to greet.

**Responses:**

- `200 OK`: A message if connected or not.
  ```json
  {
    "message": "Connected to MySQL database on host 127.0.0.1"
  }
  ```

## Build the application for Docker
```sh
# Build & Push
docker buildx build --platform linux/amd64,linux/arm64 -t josefloressv/flask_mysql_app . --push

# Run
docker run --rm --name flask-app -p 5001:5000 --env DB_HOST=host.docker.internal --env DB_USER=root --env DB_PASSWORD=root josefloressv/flask_mysql_app

```
