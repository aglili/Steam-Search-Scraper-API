from fastapi import FastAPI,Request
from utils import scrape_steam_store_data,add_price_filter,add_os,add_search,special_offers,add_tag
import uvicorn
from schema import Parameters



app = FastAPI()



@app.get("/")
def read_root():
    return {
        "name": "Steam Store Scraper",
        "version": "1.0.0",
        "description": "A simple web scraper api that extracts game data from the Steam Store.",
        "github": "https://github.com/aglili/Steam-Search-Scraper-API.git",
        "written_by": "Aglili Selorm Cecil ",
    }

@app.get("/scrape", status_code=200)
def scrape_steam_store(request: Request, parameters: Parameters):
    url = "https://store.steampowered.com/search/?category1=998&supportedlang=english"

    url_with_price_filter = add_price_filter(url, parameters.price_filter) if parameters.price_filter else url

    url_with_os = add_os(url_with_price_filter, parameters.os) if parameters.os else url_with_price_filter

    url_with_search = add_search(url_with_os, parameters.search) if parameters.search else url_with_os

    url_with_special_offers = special_offers(url_with_search, parameters.is_special_offer) if parameters.is_special_offer else url_with_search

    url_with_tag = add_tag(url_with_special_offers, parameters.tag) if parameters.tag else url_with_special_offers

    return {
        "parameters": parameters,
        "url": url_with_tag,
        "data": scrape_steam_store_data(url_with_tag),
    }



    


    

   

    