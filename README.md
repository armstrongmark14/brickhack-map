# Mark's Open Street Map Routing

Welcome to my Open Street Map routing program developed at Brickhack 4 (2018)
at RIT.

In short, it parses Open Street Map data (.osm), generates a graph of street
nodes, then finds a path between your two intersection nodes.

I made the graph generation from the .osm files a separate program because
it takes so long due to the file sizes. I also included the code to run
it directly from the .osm files if you comment out the 2 lines and uncomment 3
lines in driver.py that I identify with comments.

Note if you choose to do that: It runs significantly faster working from my
node files than straight OSM data. So ideally you use make_graph.py once to
make the graph file and then each successive run is significantly faster than
generating the graph. 

Observed straight from .osm file vs. my graph file on San Diego (~300MB file)
is:

| From map.osm File | From Graph.txt |
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
    2. Enter the first street of the first intersection inside your map area and hit enter.
    3. Enter the second street of the first intersection you chose inside your map area and hit enter.
    4. Enter the first street of the second intersection inside your map area and hit enter.
    5. Enter the second street of the second intersection you chose inside your map area and hit enter.

6. If program errors, retry the steps or redownload a new map file. Note: I got a file one time
that had a unicode character my program couldn't parse.

7. If program executes successfully, look inside the output/ folder for a file called filename.txt
where filename is the same file from steps 3 and 5.1

8. Copy the entire contents of that file, which is lines of comma separated GPS coordinates.

9. Paste the coordinates into the left-hand side of this site https://www.darrinward.com/lat-long/
to view the path my program generated between your intersections overlaid on Google Maps.

## Improvements if this was a larger project

1. I would find an xml parsing import, or write my own, that doesn't load the 
entire xml file into memory. These road maps can be huge xml files. San Diego
is one I tested with and is ~300MB, so utilizing (or writing my own) xml parser 
that only loads one node at a time would be a huge performance increase.

2. I would include edge lengths and use Dijkstra's algorithm to find the
actual shortest path instead of my Breadth First Search implementation that
only finds the path with the fewest nodes.

3. I would include highways. The OSM files I looked through have highways 
formatted differently from normal streets. If this was a larger project or I 
spent more time I would include highways.

4. I would utilize an actual method of storing the graph. Something better
than a simple text file.

5. I would implement the path finding in C++ for faster performance on large
graphs.

