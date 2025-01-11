# DigicdesTest
 
### Added Cases (`updated` Branch)
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
