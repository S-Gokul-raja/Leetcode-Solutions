def fill(image,visited,m,n,i,j,oldColor,newColor):
        visited[i][j] = True
        image[i][j] = newColor
        neighbours = [0,1,0,-1,0]
        for k in range(4):
            newI = i+neighbours[k]
            newJ = j+neighbours[k+1]
            if (0 <= newI < m) and (0 <= newJ < n) and image[newI][newJ] == oldColor:
                fill(image,visited,m,n,newI,newJ,oldColor,newColor)
def solution(image, sr, sc, newColor):
    '''
    traversing by maintaining already visited flag
    and changing the color
    '''
    m = len(image)
    n = len(image[0])
    visited = [[False for j in range(n)] for i in range(m)]
    if image[sr][sc] != newColor:
        fill(image,visited,m,n,sr,sc,image[sr][sc],newColor)
    return image
    # total time N
    # total space N