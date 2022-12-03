#### rosrun intera_interface joint_trajectory_action_server.py to have the sawyer send back information about joint states
#### roslaunch sawyer_moveit_config sawyer_moveit.launch electric_gripper:=true to run rviz/



import numpy as np

def dfs_points(grid):
    """Just takes in a grid and gives back the points in a dfs order such that they can be traversed by the robot"""
    dfs_trees = []
    notAllSeen = True
    while notAllSeen:
        notAllSeen = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    notAllSeen = True
                    listofPointsFromThisDFS = visit(grid, i, j)
                    dfs_trees.append(listofPointsFromThisDFS)
    return dfs_trees


def visit(grid, i, j):
    points = [(i, j)]
    grid[i][j] = 0
    fourDirections = [(i, j + 1), (i + 1, j), (i - 1, j), (i , j - 1)]
    for x, y in fourDirections:
        if x >= len(grid) or x < 0 or y >= len(grid[0]) or y < 0:
            continue
        if grid[x][y] == 1:
            points.extend(visit(grid, x, y))
            return points
    return points

if __name__ == '__main__':
    shape = (5, 5)
    random_grid = []
    for x in range(shape[0]):
        random_row = []
        for y in range(shape[1]):
            random_row.append(np.random.randint(0, 2))
        random_grid.append(random_row)
    print("Random Grid is ", random_grid)
    print("DFS Traversal is ", dfs_points(random_grid))
