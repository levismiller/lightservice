from flask import Flask, render_template, jsonify
import board
import neopixel
from time import sleep
from neopixel import *

pixels = neopixel.NeoPixel(board.D18, 150)

app = Flask(__name__)

fading = False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/light/<color>')
def color_change(color):
    change_color = True
    global fading
    if fading:
        return render_template('index.html')

    if color == 'favicon.ico':
        change_color = False
    else:
        fading = True
        if color == '1':
            color = (255,0,0)
        elif color == '2':
            color = (0,255,0)
        elif color == '3':
            color = (0,0,255)
        else:
            color = (0,0,0)
    
    if change_color:
        pixels.brightness = .001
        pixels.fill(color)
        pixels.show()


        bright = .001
        while bright + .01 <= 1:
            bright += .01
            pixels.brightness = bright
            sleep(.009)

        pixels.show()
        fading = False

    return render_template('index.html')
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
