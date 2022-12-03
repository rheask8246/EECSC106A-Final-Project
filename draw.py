import numpy as np

# dataflow for this module will look like this
# (1) numpy array from picture module                                   --DONE
# (2) numpy array -> DFS -> list of paths                               --DONE
# (3) list of paths -> formatting -> list of path coords                --IP (will be this code)
# (4) list of path coords -> sawyer path                                --IP (hopefully lab 7 satisfies)

# image from picture module
image = np.random.choice([0,1], size = (100,100), p = [1./3, 2./3])
image_width, image_height = image.shape

# measure the paper (in meters)
paper_width = 2
paper_height = 1

# res of each pixel on the paper
x_res = paper_width / image_width
y_res = paper_height / image_height

# distance to lift the pen after every stroke
lift_dist = .05 # TUNE

# z height of drawing plane
paper_height = 0 # CHANGE


# DFS HERE FOR PATHS #


ex_paths = np.array([[(1, 1), (1, 2)], [(1, 3), (2, 4), (2, 5)], [(2, 6)]]) #?
#                    ~~~ stroke 1 ~~~  ~~~~~~~ stroke 2 ~~~~~~~  ~~ s3 ~~
paths = ex_paths # CHANGE

# to be populated by triples (paths -> path coords)
path_coords = np.empty((paths.size,), dtype=list)

# this *should* convert paths into a list of path coords 
# with lifted stroke start and end
for i in range(paths.size):
    path = paths[i] # THIS path

    # start with lifted pen
    pen_start = (path[0][0] * x_res, path[0][1] * y_res, paper_height + lift_dist)
    path_coords[i] = np.array(pen_start)


# LAB 7 CODE BELOW #