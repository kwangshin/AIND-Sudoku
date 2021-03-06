from utils import *

assignments = []

def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """
    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """

    # Find all instances of naked twins
    # Eliminate the naked twins as possibilities for their peers

    for unit in unitlist:
        # Find the naked twins.
        nakedTwins = getNakedTwins(unit, values)
        # If the length of naked twins list is 2, then there is naked twins.
        # Otherwise, there is no naked twins in this unit.
        if(len(nakedTwins) == 2):
            # Create new targetUnit having the box list excepting 2 naked twins boxes.
            targetUnit = unit.copy()
            targetUnit.remove(nakedTwins[0])
            targetUnit.remove(nakedTwins[1])
            # Remove 2 digits which are in naked twins box from target boxes.
            for box in targetUnit:
                for digit in values[nakedTwins[0]]:
                    value = values[box].replace(digit,'')
                    values = assign_value(values, box, value)

    return values

def getNakedTwins(unit, values):
    """
    Get naked twins from the unit.
    Args:
        unit(list) - One unit in list form of box.
        values(dict): a dictionary of the form {'box_name': '123456789', ...}
    Returns:
        A list with 2 boxes, if there is naked twins
            For example, ['A1','A5']
        A empty list, if there is no naked twins
            For example, []
    """
    nakedTwins = []

    for box in unit:
        # Create temporary unit excepting the box-itself.
        tempUnit = unit.copy()
        tempUnit.remove(box)
        for targetBox in tempUnit:
            firstBoxValue = values[box]
            secondBoxValue = values[targetBox]
            # Compare 2 boxes value and length with 2
            if(firstBoxValue == secondBoxValue and len(firstBoxValue) == 2):
                # We found the naked twins!
                nakedTwins.append(box)
                nakedTwins.append(targetBox)
                return nakedTwins
                
    return nakedTwins

# def cross(A, B):
#     "Cross product of elements in A and elements in B."
#     return [s+t for s in A for t in B]

def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    values = []
    all_digits = '123456789'
    for c in grid:
        if c == '.':
            values.append(all_digits)
        elif c in all_digits:
            values.append(c)
    assert len(values) == 81
    return dict(zip(boxes, values))

def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    print

def eliminate(values):
    # Find all solved values, i.e., only one possible value in box.
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    for box in solved_values:
        # If the box is solved, then the digit in box is not able to appear in peers of the box.
        digit = values[box]
        for peer in peers[box]:
            # Remove the digit from the value of peers.
            value = values[peer].replace(digit,'')
            values = assign_value(values, peer, value)
    return values

def only_choice(values):
    new_values = values.copy()
    for unit in unitlist:
        # Check all digits one by one from the unit.
        for digit in '123456789':
            dplaces = [box for box in unit if digit in values[box]]
            # If the digit is appeared only once in the unit, 
            #   then the box is considered as solved with the digit.
            if len(dplaces) == 1:
                new_values[dplaces[0]] = digit
    return new_values

def reduce_puzzle(values):
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    stalled = False
    while not stalled:
        # Check how many boxes have a determined value
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
        # Use the Eliminate Strategy
        values = eliminate(values)
        # Use the Naked Twins Strategy
        values = naked_twins(values)
        # Use the Only Choice Strategy
        values = only_choice(values)
        # Check how many boxes have a determined value, to compare
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        # If no new values were added, stop the loop.
        stalled = solved_values_before == solved_values_after
        # Sanity check, return False if there is a box with zero available values:
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values

def search(values):
    values = reduce_puzzle(values)
    if values is False:
        return False ## Failed earlier
    if all(len(values[s]) == 1 for s in boxes): 
        return values ## Solved!
    # Choose one of the unfilled squares with the fewest possibilities
    n,s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)
    # Now use recurrence to solve each one of the resulting sudokus, and 
    for value in values[s]:
        new_sudoku = values.copy()
        new_sudoku[s] = value
        attempt = search(new_sudoku)
        if attempt:
            return attempt

def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """

    values = search(grid_values(grid))

    return values;

if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
