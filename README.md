# percolator-3000
Exploration of basic percolation properties and related algorithms.


#### Running the script
In order to run, make sure to have manim installed. Then run with ```manim -p -ql main.py PercolationDemo```, where ```-ql``` stands for low quality, so that can be changed to ```-qh```, for example. It will increase rendering time, but will produce a higher quality video.
Another requirement are the ffmpeg codecs required by manim.

#### What to expect
Once you run the script, you will see a 10x10 grid rendered with matplotlib. On it, green cells show where percolation occured from the top to bottom. Any adjacent cells (but not in diagonal) that form a path will be colored green.
Afterwards, you have to close the matplotlib window to let manim begin rendering. A short while later, rendered video should open, showing the same grid, but animated, showing the recursive process of coloring the cells.
