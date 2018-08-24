class FindMax:
  def array(self,array):
    self.array = array
    self.visited = []
    self.tovisit = [[0,0]]

  def MaxForCurrentCoordinates(self, x,y):
      count = 0
      if [x,y] not in self.visited:
          self.visited.append([x,y])
          
          try:
              if self.array[x][y] == self.array[x+1][y]:
                  count = 1 + self.MaxForCurrentCoordinates(x+1, y)
                  
              else:
                  count = 1
                  if [x+1,y] not in self.tovisit and [x+1,y] not in self.visited:
                      self.tovisit.append([x+1,y])
          except:
              count += 1
              
          try:
                  
              if self.array[x][y] == self.array[x][y+1]:
                  count += self.MaxForCurrentCoordinates(x, y+1)
              
              else:
                  if [x,y+1] not in self.tovisit and [x,y+1] not in self.visited:
                      self.tovisit.append([x,y+1])
                  
          except:
              pass
          
          try:
              if (x-1)>=0:
                  
                  if self.array[x][y] == self.array[x-1][y]:
                      count += self.MaxForCurrentCoordinates(x-1,y)
                  
                  else:
                      if [x-1,y] not in self.tovisit and [x-1,y] not in self.visited:
                          self.tovisit.append([x-1,y])
          except:
              pass
          
          try:
              if (y-1)>=0:
                  if self.array[x][y-1] == self.array[x][y]:
                      count += self.MaxForCurrentCoordinates(x,y-1)
                  
                  elif x!=0 and y-1!=0:
                      self.tovisit.append([x][y-1])
          
          except:
              pass
          
      return count


  def FindMaxNow(self):
      self.visited = []
      self.tovisit = [[0,0]]
      mcount = 0
      while self.tovisit:
          x , y = self.tovisit.pop()
          if [x,y] not in self.visited:
              count = self.MaxForCurrentCoordinates(x,y)
              if mcount < count:
                  mcount = count
      
      return mcount

  def FindMaxElement(self):
      mcount = 0
      element = ''
      while self.tovisit:
          x , y = self.tovisit.pop()
          if [x,y] not in self.visited:
              count = self.MaxForCurrentCoordinates(x,y)
              if mcount < count:
                  mcount = count
                  element = self.array[x][y]
              
              elif mcount == count:
                  
                  if type(element) is int:
                      element = [element]
                  element.append(self.array[x][y])
                 
      return element
      

if __name__ == "__main__":
    n = int(input())
    array = list()
    for i in range(n):
        array.append(list(map(int, input().split())))


    object = FindMax()
    object.array(array)
    print(object.FindMaxElement(),object.FindMaxNow())
