from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

for x in range(0, 800, 5):
    clear_canvas()      # 백 버퍼를 지운다
    grass.draw(400,30)  # draw는 백버퍼에 그린다
    character.draw(x, 90)
    update_canvas()     # 두 개의 버퍼르 교환한다.
    delay(0.01)

close_canvas()

