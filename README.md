# Engine2D
The Engine2D project that uses Pytest and Tkinter. <br>
It provides an engine that can draw various shapes such as Triangles, Rectangles, and Circles, and display them on a canvas widget from Tkinter.<br>
Additionally, it includes a method to change the color of the drawn shapes.<br>

to install the required dependencies, run the following command in the terminal:<br>
`pip install -r requirements.txt`<br>

## Tests
Tests are divided into two groups: engine and canvas.

To test the engine group, run the following command in the terminal:<br>
`pytest --rootdir=tests -s -v --tb=long -m engine`<br>
To test the canvas group, run the following command in the terminal:<br>
`pytest --rootdir=tests -s -v --tb=long -m canvas`<br>
To run all tests at once, use the following command:<br>
`pytest --rootdir=tests -s -v --tb=long`<br>
