import tkinter
import random
ROWS=25
COLS=25
TILE_SIZE=25
WINDOW_WIDTH=TILE_SIZE*COLS
WINDOW_HEIGHT=TILE_SIZE*ROWS
class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

root=tkinter.Tk()
root.title("Snake Game")
root.resizable(False, False)
canvas=tkinter.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg="black",borderwidth=0, highlightthickness=0)
canvas.pack()
root.update()

window_width = root.winfo_width()
window_height= root.winfo_height()
screen_width= root.winfo_screenwidth()
screen_height= root.winfo_screenheight()
window_x= int((screen_width/2)-(window_width/2))
window_y= int((screen_height/2)-(window_height/2))
root.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")
root.update()

snake=Tile(TILE_SIZE*5, TILE_SIZE*5)
food=Tile(TILE_SIZE*10, TILE_SIZE*10)
VelocityX=0
VelocityY=0 
snake_body=[]
game_over=False
score=0

def change_direction(e):
    global VelocityX, VelocityY, game_over
    if game_over:
        return
    elif e.keysym=="Up" and VelocityY!=1:
        VelocityX=0
        VelocityY=-1
    if e.keysym=="Down" and VelocityY!=-1:
        VelocityX=0
        VelocityY=1
    if e.keysym=="Left" and VelocityX!=1:
        VelocityX=-1
        VelocityY=0
    elif e.keysym=="Right" and VelocityX!=-1:
        VelocityX=1
        VelocityY=0

def move():
    global snake,food,snake_body,game_over,score
    if game_over:
        return
    if (snake.x < 0 or snake.x >= WINDOW_WIDTH or snake.y >= WINDOW_HEIGHT):
        game_over=True
        return
    for tile in snake_body:
        if snake.x == tile.x and snake.y == tile.y:
            game_over= True
            return

    if (snake.x==food.x and snake.y==food.y):
        snake_body.append(Tile(food.x, food.y))
        food.x=random.randint(0, COLS-1)*TILE_SIZE
        food.y=random.randint(0, ROWS-1)*TILE_SIZE
        score=score+1
    for i in range(len(snake_body)-1,-1,-1):
        tile=snake_body[i]
        if i==0:
            tile.x=snake.x
            tile.y=snake.y
        else:
            prev_tile=snake_body[i-1]
            tile.x=prev_tile.x
            tile.y=prev_tile.y
    snake.x+=VelocityX*TILE_SIZE
    snake.y+=VelocityY*TILE_SIZE
def draw():
    global snake,food,snake_body,game_over,score
    move()
    canvas.delete("all")
    canvas.create_rectangle(food.x, food.y, food.x + TILE_SIZE, food.y + TILE_SIZE, fill="white")
    canvas.create_rectangle(snake.x, snake.y, snake.x + TILE_SIZE, snake.y + TILE_SIZE, fill="blue")
    for Tile in snake_body:
        canvas.create_rectangle(Tile.x, Tile.y, Tile.x + TILE_SIZE, Tile.y + TILE_SIZE, fill="blue")
    if game_over:
        canvas.create_text(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, text=f"Game Over\n  Score: {score}", fill="white", font=("Arial", 25))
    else:
        canvas.create_text(30,20, text=f"Score: {score}", fill="white", font=("Arial", 10))
    root.after(100,draw)
draw()
root.bind("<KeyRelease>", change_direction)
root.mainloop()
