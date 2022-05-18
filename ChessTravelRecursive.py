"""
Recursive function to calculate chess moves given initial pos then objective
rules: a move can only be up or right.
completed and steps values start à 0
for more clarity, you can refacto that and use those as global variables
for this:
    uncomment every line commented
    if there is a line strictly under it, comment it

completed give number of path
steps is extra variable to search for correlation between numbers (don't pay attention to it)
"""

# completed = 0
# steps = 0

# def crawl(pos, obj, silence=True):
def crawl(pos, obj, completed=0, steps=0, silence=True):
    # global completed
    # global steps
    
    if not silence:
        print('started a crawl at ', pos)
        print('current steps: ', steps)
    

    if pos[0] < obj[0]:
        newPos = [pos[0], pos[1]]
        newPos[0] += 1
        steps += 1
        # crawl(newPos, obj)
        completed, steps = crawl(newPos, obj, completed, steps)

    if pos[1] < obj[1]:
        newPos = [pos[0], pos[1]]
        newPos[1] += 1
        steps += 1
        # crawl(newPos, obj)
        completed, steps = crawl(newPos, obj, completed, steps)

    if pos == obj:
        completed += 1
        print('current completed: ', completed)

    # return
    return completed, steps

initial = [1,1]
objective = [3,3]

# crawl(initial, objective)
completed, steps =  crawl(initial, objective)
print(completed)
print(steps)

### verified results for testing ###

#'(1 1)(3 3)' => 6
#'(1 1)(4 3)' => 10
#'(1 1)(3 4)' => 10
#'(1 1)(5 3)' => 15
#'(1 1)(3 7)' => 28
#'(1 1)(4 4)' => 20
#'(1 1)(5 5)' => 70
#'(1 1)(6 6)' => 252
#'(1 1)(7 7)' => 924
#'(1 1)(8 8)' => 3432
