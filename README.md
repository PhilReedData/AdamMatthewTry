# AdamMatthewTry
Try using the API for data mining with Adam Matthew Digital databases (requires subscription to AM Digital)

First attempt will use Python.

## Requires
- A subscription to Adam Matthew Digital products such as Mass Observation
- An API key for their data mining features

## To run:
![Script](img/script.png)
- Download these files to your computer.
- Edit `read_test.py` and __replace the `apiKey` value__ from `XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX` to the correct value.
  - The image above shows _Notepad_. A better text editor to use is _Notepad++_.
- If you are familiar with using the command line, change to this directory and call `python read_test.py`
- If not, and you are using Windows:

Open Explorer at the __AdamMatthewTry__ directory.

![Explorer](img/shift-right-click.png)

In the white space in the middle of the window (below the list of file names), hold Shift and right-click, choose __Open command window here__.

![Command window](img/command-window.png)

In the command window, type `python read_test.py` and press Enter.

![Command window response](img/command-window-response.png)

The returned JSON code will show in the command window. There will be a `u` character before each string (piece of text), meaning that the text is Unicode not ASCII -- this will become important later.

## Going further
- You can edit the URL as per the [Adam Matthew API documentation](http://developers.amdigital.co.uk/API/Overview) to get more, desirable responses.
- You can find better ways to use the reponses, such as exporting to CSV. 
  - You can do this by uncommenting the last five lines in the script, i.e. deleting the `#` symbol from the start of those lines (from `import csv` onwards), then running again. 
  - A new output file will be created `mycsvfile.csv` which can be opened in Excel.
- You can extend the Python script to do other things such as retrieve the full-text for multiple items, store the text to a local database (your own new corpus), then perform analysis on the corpus.