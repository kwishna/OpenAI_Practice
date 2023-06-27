getprice_meta_data = {
    "name": "get_price",
    "description": "Get The Closing Price Of An Stock For The Date Provided.",
    "parameters": {
        "type": "object",
        "properties": {
            "symbol": {
                "type": "string",
                "description": "The Company Symbol For Which Closing Stock Price To Be Fetched."
            },
            "date": {
                "type": "string",
                "description": "Date for which closing price of stock to be fetched in YYYY-MM-DD format."
            }
        },
        "required": ["symbol", "date"],
    }
}
