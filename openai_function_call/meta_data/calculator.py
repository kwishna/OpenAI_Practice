calculate_metadata = {
    "name": "calculate",
    "description": "Calculate The Result Of Operation On Two Floating Point Numbers.",
    "parameters": {
        "type": "object",
        "properties": {
            "a": {
                "type": "number",
                "description": "First floating point number for the operation."
            },
            "b": {
                "type": "number",
                "description": "Second floating point number for the operation."
            },
            "op": {
                "type": "string",
                "enum": ["sum", "truediv", "mul", "sub"],
                "description": "Operation to be performed on both the floating point numbers"
            }
        },
        "required": ["a", "b", "op"]
    }
}
