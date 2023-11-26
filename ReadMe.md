# Steam Store Scraper API Documentation

## Introduction
This API serves as a web scraper for extracting game data from the Steam Store. It provides endpoints to fetch game information based on different parameters.

## Base URL
The base URL for this API is `https://steam-search-scraper-api-production.up.railway.app`.

## Endpoints

### GET /
- **Description:** Get information about the Steam Store Scraper API.
- **Usage:** Send a GET request to the base URL.
- **Response Example:**
    ```json
    {
        "name": "Steam Store Scraper",
        "version": "1.0.0",
        "description": "A simple web scraper API that extracts game data from the Steam Store.",
        "github": "https://github.com/aglili/Steam-Search-Scraper-API.git",
        "written_by": "Aglili Selorm Cecil"
    }
    ```

### GET /scrape
- **Description:** Scrape game data from the Steam Store based on parameters.
- **Usage:** Send a GET request to `/scrape` with query parameters.
- **Parameters:**
    - `price_filter`: Filter games by price range (e.g., `under_10`, `under_15`, etc.).
    - `os`: Filter games by operating system (e.g., `windows`, `mac`, `linux`).
    - `search`: Search for games by a specific term.
    - `is_special_offer`: Filter games with special offers (e.g., `True` or `False`).
    - `tag`: Filter games by tag (e.g., `Action`, `Adventure`, etc.).
- **Response Example:**
    ```json
    {
        "parameters": {
            "price_filter": "under_15",
            "os": "windows",
            "search": "strategy",
            "is_special_offer": true,
            "tag": "Strategy"
        },
        "url": "https://store.steampowered.com/search/?category1=998&supportedlang=english&maxprice=15&term=strategy",
        "data": [ ... ]  // Game data extracted from the Steam Store
    }
    ```

## How to Use
1. **GET `/`**: Use this endpoint to get information about the API itself.
2. **GET `/scrape`**: Use this endpoint to scrape game data from the Steam Store based on the provided parameters. Pass query parameters to filter the games based on your preferences.

## Example Usage
GET `/scrape?price_filter=under_15&os=windows&search=strategy&is_special_offer=True&tag=Strategy`
This request will fetch strategy games under $15 available for Windows OS with special offers tagged as 'Strategy'.


## How to Use the API Documentation (/docs)

1. Open a web browser.
2. Visit the URL: `https://steam-search-scraper-api-production.up.railway.app/docs`
3. Explore the available endpoints, parameters, and schemas.
4. Test the API by providing parameters and making requests directly from the browser interface.

Feel free to explore the interactive API documentation to understand the available endpoints and how to interact with them.
