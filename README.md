# DigicdesTest
 
# Farmer Info API

This project provides a simple Flask-based REST API to manage farmer information. The API supports adding farmer details, retrieving all farmer records, and fetching specific records based on farmer IDs. The database is managed using SQLAlchemy with migrations enabled through Flask-Migrate.

## Branch Descriptions

### `main` Branch
This branch contains the initial implementation of the Farmer Info API:
- **Database Model**:
  - `FarmerInfo` model with fields for `id`, `name`, `location`, `number`, and `PINcode`.
- **Endpoints**:
  - `POST /info`: Allows adding a new farmer record.
- **Key Features**:
  - Basic database model setup using SQLAlchemy.
  - API endpoint to insert farmer details into the database.

### `updated` Branch
This branch builds upon the `main` branch and introduces the following enhancements:
1. **Unique Constraint**:
   - Added a unique constraint on the `number` field to ensure no duplicate phone numbers are stored.
2. **Error Handling**:
   - Implemented simple `try-except` blocks to gracefully handle common errors such as:
     - Missing required fields.
     - Unique constraint violations (duplicate phone numbers).
     - General server errors.
3. **New Endpoints**:
   - `GET /info`: Retrieves all farmer records.
   - `GET /info/<int:farmer_id>`: Retrieves a specific farmer record by ID.
4. **Database Migrations**:
   - Enabled database migrations using Flask-Migrate to handle schema changes.

## Approach

### Initial Implementation (`main` Branch)
1. **Objective**:
   - Create a basic API to store farmer details in a PostgreSQL database.
2. **Steps**:
   - Set up Flask and SQLAlchemy.
   - Define the `FarmerInfo` model with basic fields (`id`, `name`, `location`, `number`, `PINcode`).
   - Implement a single endpoint (`POST /info`) to accept farmer data and save it to the database.

### Enhanced Implementation (`updated` Branch)
1. **Objective**:
   - Improve the initial implementation by adding error handling, a unique constraint, and new endpoints for retrieving farmer records.
2. **Steps**:
   - **Add Unique Constraint**:
     - Updated the `number` field to enforce uniqueness in the database.
     - Used Flask-Migrate to handle schema changes.
   - **Error Handling**:
     - Validated request data for required fields.
     - Caught errors for duplicate phone numbers and other server issues.
   - **New Endpoints**:
     - Created a `GET` endpoint to retrieve all farmers.
     - Enhanced the `GET` endpoint to support fetching a specific farmer by ID directly from the URL.
   - **Database Migrations**:
     - Added migrations to ensure the unique constraint and schema changes were applied without losing data.

## Usage

### Running the API
1. Clone the repository and switch to the desired branch (`main` or `updated`).
2. Start the virtual Environment:
   ```bash
   venv\Scripts\Activate.ps1
   ```
3. Set up the database:
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```
4. Run the application:
   ```bash
   python app.py
   ```
### Endpoints

#### POST /info
Adds a new farmer record.
```json
{
    "name": "Dhruvrajsinh",
    "location": "Ahmedabad",
    "number": "9856231475",
    "PINcode": "123456"
}
```
Response:
Success: 201 Created
Error: 400 Bad Request or 500 Internal Server Error

#### GET /info
Retrieves all farmer records.
Success: 200 OK
Example:
```json
[
    {
        "id": 1,
        "name": "Dhruvrajsinh",
        "location": "Ahmedabad",
        "number": "9856231475",
        "PINcode": "123456"
    }
]
```
#### GET /info/<int:farmer_id>
Retrieves a specific farmer record by ID.
