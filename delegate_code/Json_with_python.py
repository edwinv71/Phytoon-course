'''
models are scripts imoortetd for use in other scripts'''
'''widget": {
    "debug": "on",
        "window": {
            "title": "Sample Konfabulator Widget",
            "name": "main_window",
            "width": 500,
            "height": 500
        },
        "image": { 
            "src": "Images/Sun.png",
            "name": "sun1",
            "hOffset": 250,
            "vOffset": 250,
            "alignment": "center"
        },
        "text": {
            "data": "Click Here",
            "size": 36,
            "style": "bold",
            "name": "text1",
            "hOffset": 250,
            "vOffset": 100,
            "alignment": "center",
            "onMouseUp": "sun1.opacity = (sun1.opacity / 100) * 90;"
        }
    }
}'''



import json
books =[  
    {'title': 'The Gruffalo', 'author': 'Julia Donaldson'},
    {'title': 'The Twits', 'author': 'Roald Dahl'},
    {'title': 'The Bippolo Seed', 'author': 'Dr. Seuss'}]

#python to JSON : json.dumps

books_json = json.dumps(books)
print(books_json)