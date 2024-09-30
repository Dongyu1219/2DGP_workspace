from pico2d import *

open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')


# fill here
running = True

def handle_events():
    # fill here
    # running 은 글로벌 변수임을 알려줌. running이 밖에서 정의된 변수이다:
    global running #이 문장을 지운다면 작동은 되는데 나가지지 않는다. 함수 밖 running에 영향을 미치지 않는다

    events = get_events()           # events: List

    for event in events:            # 여러 이벤트 중 하나
        if event.type == SDL_QUIT:
            running = False
        elif event.type== SDL_KEYDOWN and event.key == SDLK_ESCAPE:     #escape 키 눌림
            running = False

    pass


frame = 0
for x in range(0, 800, 5):

    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 100, 100, 100, x, 90)
    update_canvas()

    # fill here
    handle_events()
    if not running:     #running 이 false면 for 문 나간다 ---> running: 루프 제어 변수
        break

    frame = (frame + 1) % 8
    delay(0.05)


close_canvas()
