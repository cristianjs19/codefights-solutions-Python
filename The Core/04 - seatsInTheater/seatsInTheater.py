def seatsInTheater(nCols, nRows, col, row):
    
    tCols = nCols - col + 1
    tRows = nRows - row
    
    return tCols * tRows
