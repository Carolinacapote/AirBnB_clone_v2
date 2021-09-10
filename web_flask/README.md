# 0x04. AirBnB clone - Web framework

## Description

This file contains some tasks related to web frameworks. For this project I am going to use Flask as a web framework and jinja as template.

### Files description

- **__init__.py:**  
Start point
  
- **0-hello_route.py:**  
Script that starts a Flask web application.
  
- **1-hbnb_route.py:**  
Script that starts a Flask web application.
   - Routes: 
    1. /: display “Hello HBNB!”
    2. /hbnb: display “HBNB”
    
- **2-c_route.py:**  
Same as **1-hbnb_route.py** including the route -> /c/<text>: display “C ” followed by the value of the text variable (replace underscore _ symbols with a space )
  
- **3-python_route.py:**  
Same as **2-c_route.py:** including the route -> /python/(<text>): display “Python ”, followed by the value of the text variable.
  
- **4-number_route.py:**  
Same as **3-python_route.py** including the route -> /number/<n>: display “n is a number” only if n is an integer.
  
- **5-number_template.py** and **templates/5-number.html:**  
Same as **4-number_route.py** including the route -> /number_template/<n>: display a HTML page only if n is an integer.
  
- **6-number_odd_or_even.py** and **templates/6-number_odd_or_even.html:**  
Same as **5-number_template.py** including the route -> /number_odd_or_even/<n>: display a HTML page only if n is an integer.
  
- **7-states_list.py** and **templates/7-states_list.html:**  
Write a script that starts a Flask web application.
  - /states_list: display a HTML page
  - After each request, remove the current SQLAlchemy Session.
  - `storage` for fetching data from the storage engine
  
- **8-cities_by_states.py** and **templates/8-cities_by_states.html:**  
Script that starts a Flask web application.
  - To load all cities of a State.
  - After each request, remove the current SQLAlchemy Session.
  - /cities_by_states: display a HTML page.
  
- **9-states.py** and **templates/9-states.html:**  
Script that starts a Flask web application.
  - To load all cities of a State.
  - /states: display a HTML page.
  - /states/<id>: display a HTML page.
  
- **10-hbnb_filters.py**, **templates/10-hbnb_filters.html** and **static/**  
Routes:
  - /hbnb_filters: display a HTML page like [6-index.html](https://github.com/Carolinacapote/AirBnB_clone_v2/blob/master/web_static/6-index.html)
  - Copy files 3-footer.css, 3-header.css, 4-common.css and 6-filters.css from web_static/styles/ to the folder web_flask/static/styles
  - Copy files icon.png and logo.png from web_static/images/ to the folder web_flask/static/images
  - State, City and Amenity objects must be loaded from DBStorage.
  
## Author

| Name | GitHub username |
| ------ | ------ |
| Carolina Capote | [Carolinacapote](https://github.com/Carolinacapote) |
