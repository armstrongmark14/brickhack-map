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
node files than straight OSM data.

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

