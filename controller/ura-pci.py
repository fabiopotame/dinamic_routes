from flask import jsonify

def GET_calls(id, form):
    response = {
    "items": [
    	{
    	"card": {
    		"bin": "452036",
    		"last_digits": "4256"
    	}
    	}
    ]
    }
    return response