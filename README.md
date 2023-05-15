# Engine2D
The project that uses Pytest, Tkinter

Engine that can draw Triangles, Rectangles, Circles and show it on canvas widget from tkinter
It can change color via method change_color

Tests are separated in groups: engine, canvas
To test a group input in terminal: 
pytest --rootdir=tests -s -v --tb=long -m engine
or
pytest --rootdir=tests -s -v --tb=long -m canvas

To start all tests input in terminal: 
pytest --rootdir=tests -s -v --tb=long
