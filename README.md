# Book Manager

## Overview
The Book Manager is a database-driven application designed to manage a collection of books and their associated publishers. It offers functionality to add, edit, delete, and search for books using various criteria. This project utilizes a MySQL database to store book and publisher information and features a user-friendly text-based interface.

## Functional Requirements
- **Add a New Publisher:** Users can add publishers with details such as name, phone number, and city.
- **Add a New Book:** Users can add books with details including ISBN, title, year, publisher, previous edition, and price.
- **Edit an Existing Book:** Books already in the database can be edited.
- **Delete a Book:** Books can be removed from the database.
- **Search Books:** Users can search for books based on:
  1. All books
  2. Title
  3. ISBN
  4. Publisher
  5. Price range (minimum and maximum)
  6. Year of publication
  7. Combination of title and publisher

## Database Schema
- **Publisher:** `name, phone, city` (Primary Key: `name`)
- **Book:** `ISBN, title, year, published_by, previous_edition, price` (Primary Key: `ISBN`, Foreign Key: `published_by` references `Publisher`, `previous_edition` references `Book`)

## Installation
1. Clone the repository from GitHub.
2. Navigate to the `Project-1` directory.
3. Run the `schema-creation.sql` script to create and populate the database:
4. Run menu.py to start the program
