# Brickhack 4 (2018) Project: Open Street Map Routing 

Welcome to my Open Street Map routing program developed in under 24 hours at Brickhack 4 (2018)
at RIT.

In short, it asks for 4 street names that form 2 intersections then parses Open Street Map data (.osm),
generates a graph of nodes, and finally finds the shortest path between your two GPS coordinates.

I made the graph generation from the .osm files a separate program because
it takes so long due to the large file sizes. I also included the code to run
it directly from the .osm files if you comment out the 2 lines and uncomment 3
lines in driver.py that I identify with comments.

Note if you choose to do that: It runs significantly faster working from my
node files than straight OSM data. So ideally you use make_graph.py once to
make the graph file and then each successive run is significantly faster than
generating the graph.

Observed straight from .osm file vs. my graph file on San Diego (~300MB file)
is:

| From map.osm File | From graph.txt |
------------------- | -------------- |
| ~30 seconds       | ~3 seconds     |

## How to Operate the program

1. Download the code or clone the repository.

2. Download .osm data from https://mapzen.com/data/metro-extracts/ or
https://www.openstreetmap.org/ and move the .osm file into the maps/ folder.

3. Navigate to the program's root directory and run make_graph.py and when prompted, type the name of your map file without
the .osm and hit enter.

4. Check your graphs/ folder and make sure you have a file with filename.txt, 
where filename is the name you typed after running make_graph.py.

5. Navigate to the program's root directory and run driver.py.

    1. Enter the same filename you used above.
    2. Format for the GPS coordinates is: 12.345678, 12.345678
    3. Enter the GPS coordinates of your first point.
    4. Enter the GPS coordinates of your second point.

6. If the program errors, retry the steps or download a new map file to try.

7. If the program executes successfully, look inside the output/ folder for a file called filename.txt
where filename is the same file from steps 3 and 5.1.

8. Copy the entire contents of that file, which consists of comma separated latitude and longitude GPS coordinates.

9. Paste the coordinates into the left-hand side of this site https://www.darrinward.com/lat-long/
to view the path my program generated between your intersections overlaid on Google Maps.

10. Use the generated link in the terminal to compare the generated route to ones that Google Maps chooses.

## Improvements I would make if this was a larger project

1. Fnd an xml parsing import, or write my own, that doesn't load the 
entire xml file into memory. These road maps can be huge xml files. The .osm file for San Diego
is ~300MB and takes awhile but runs, San Francisco was ~1.4GB and my computer completely locked up, 
so utilizing (or writing my own) xml parser that only loads one node at a time would be a huge performance increase.

2. Utilize an actual method for storing the graph. Something better
than a simple text file.

3. Implement the path finding in C++ for faster performance on large
graphs.

