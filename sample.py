from  flask import Flask,render_template
import json

app = Flask(__name__)

devices = {
            "led": "on",
            "door": "open"
           }
@app.route("/")
def main():
    return render_template("index.html")

#led on
@app.route("/led_on")
def led_on():
   
    devices['led'] = "on"
    return render_template("index.html")

#led off
@app.route("/led_off")
def led_off():
    
    devices['led'] = "off"
    return render_template("index.html")

#door open
@app.route("/door_open")
def door_open():
    devices['door'] = "open"
    return render_template("index.html")

#door close
@app.route("/door_close")
def door_close():
    devices['door'] = "close"
    return render_template("index.html")



#dht on
@app.route("/dht_on")
def dht_on():
    devices['dht'] = "on"
    return render_template("index.html")

#dht off
@app.route("/dht_off")
def dht_off():
    devices['dht'] = "off"
    return render_template("index.html")

# buzzer off
@app.route("/buzzer_on")
def buzzer_on():
    devices['buzzer'] = "on"
    return render_template("index.html")

# buzzer off
@app.route("/buzzer_off")
def buzzer_off():
    devices['buzzer'] = "off"
    return render_template("index.html")

# smoke_detector on
@app.route("/gas_detector_on")
def gas_detector_on():
    devices['gas_detector'] = "on"
    return render_template("index.html")

# smoke_detector off
@app.route("/gas_detector_off")
def gas_detector_off():
    devices['gas_detector'] = "off"
    return render_template("index.html")

#get values
@app.route("/get_values")
def get_values():
    return json.dumps(devices)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5001, debug=True)

