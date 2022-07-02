"""
-- Implement for simulation --
"""
row,column=map(int,input().split()) 
current_x,current_y,dir=map(int,input().split())


### save as 북서남동 해당 좌표
possible_x=[0,-1,0,1]
possible_y=[-1,0,1,0]

map_info=[]

for i in range(row):
  each_row_info=list(map(int,input().split()))
  while True:
    if len(each_row_info)==column:
      map_info.append(each_row_info)
      break
    else:
      each_row_info=list(map(int,input().split()))

## inital visited
map_info[current_x][current_y]=1
count=1

chance=0

## direction change
def roate_direction():
  global dir
  dir+=1
  if dir==4:
    dir=0

while True:
  roate_direction()
  new_dx=current_x+possible_x[dir]
  new_dy=current_y+possible_y[dir]
  if map_info[new_dx][new_dy]==0:
    current_x=new_dx
    current_y=new_dy
    count+=1
    chance=0
    map_info[new_dx][new_dy]=1
  else:
    chance+=1

  if chance==4:
    new_dx=current_x-possible_x[dir]
    new_dy=current_y-possible_y[dir]
    if map_info[new_dx][new_dy]==0:
      current_x=new_dx
      current_y=new_dy
      count+=1
      chance=0
      map_info[new_dx][new_dy]=1
    else:
      break


print('count',count)