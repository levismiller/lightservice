from flask import Flask, render_template, jsonify
import board
import neopixel
from time import sleep
from neopixel import *

pixels = neopixel.NeoPixel(board.D18, 150)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/light/<color>')
def color_change(color):
    change_color = True

    if color == 'favicon.ico':
        change_color = False
    else:

        if color == '1':
            color = (255,0,0)
        elif color == '2':
            color = (0,255,0)
        elif color == '3':
            color = (0,0,255)
        else:
            color = (0,0,0)
    
    if change_color:
        pixels.brightness = .01
        pixels.fill(color)
        pixels.show()


        bright = .01
        while bright + .01 <= 1:
            bright += .01
            pixels.brightness = bright
            sleep(.005)

        pixels.show()

    return render_template('index.html')
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
