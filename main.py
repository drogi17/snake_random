from skins import skins
import random, time, os
os.system('clear')

skin = skins.get('colors')
speed = 0.08

def main(skin):
    if skin.get('colored'):
        skin.get('colors').append('')
    pos_now = 0
    color_num = 0
    back = skin['back']
    body = skin['body']
    end = skin['end']
    while True:
        width = int(os.popen('stty size', 'r').read().split()[1])-3
        pos_to = random.randint(0, width)
        if pos_to > pos_now:
            for _ in range(pos_now):
                print(' ', end='')
            print(back, end='')
            pos_now += 1
            while pos_now < pos_to:
                pos_now += 1
                # print(color_num)
                if skin.get('colored'):
                    if color_num > len(skin.get('colors'))-1 or color_num+1 > len(skin.get('colors'))-1:
                        color_num = 0
                    start_color = skin.get('colors')[color_num]
                    end_color = skin.get('colors')[color_num+1]
                    color_num += 1
                    print( start_color + body + end_color, end='')
                else:
                    print(body, end='')
            print(end, end='')
        elif pos_to < pos_now:
            for _ in range(pos_to):
                print(' ', end='')
            print(end, end='')
            pos_now -= 1
            while pos_to < pos_now:
                pos_now -= 1
                if skin.get('colored'):
                    if color_num > len(skin.get('colors'))-1 or color_num+1 > len(skin.get('colors'))-1:
                        color_num = 0
                    start_color = skin.get('colors')[color_num]
                    end_color = skin.get('colors')[color_num+1]
                    color_num += 1
                    print( start_color + body + end_color, end='')
                else:
                    print(body, end='')
            print(back, end='')
        if skin.get('indent'):
            print('')
            for _ in range(pos_now):
                print(' ', end='')
            print(body)
        else:
            print('')
        time.sleep(0.02)

if __name__ == '__main__':
    try:
        main(skin)
    except KeyboardInterrupt:
        print('Stoped')