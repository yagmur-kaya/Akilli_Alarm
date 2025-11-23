# SmartGuard Sensor System
The main purpose of this project is to measure temperature, light, and water levels in a home environment through sensors, and to alert the user and enable necessary precautions when predefined threshold values are exceeded.
## Project Description
In this project, ambient temperature, light, and water level values were measured using an Arduino via a DHT11 (temperature-humidity sensor), LDR (light sensor), and a water level sensor. The collected data was transferred to a computer using Python, analyzed using the pandas and matplotlib libraries, and visualized with various graphs.
Alarm events that occurred when certain threshold values were exceeded were recorded, and the distribution of these alerts was shown with a pie chart. Additionally, the data was archived by saving it to CSV files daily.
Thanks to the RTC (Real Time Clock) module used in the project, instant time information was read, and a timestamp was added to every data record. Furthermore, the date and time information, along with the sensor data, were displayed in real-time on the LCD I2C screen.
To evaluate the system's general status, the average values of the obtained sensor measurements were also calculated and reported.
## Used Technologies
Hardware: Arduino Uno, breadboard, buzzer, RGB LED, three 220 ohm resistors, one 10k resistor, DHT11 sensor, LDR, water level sensor, RTC module, LCD I2C screen, and jumper cables. 
Software: Arduino IDE, Python. 
Python Libraries: serial, time, pandas, matplotlib, os, datetime.
# Setup and Usage
## Development Phase
Set Up the Circuit: Place the specified circuit components on the breadboard according to the schematic and make the connections.
Install Necessary Libraries: Install the pyserial library for Python via the terminal using the pip install pyserial command.
Prepare the Code: Write both the Arduino and Python code required for the project.
## Application Phase
Prepare the Hardware: After setting up the circuit, connect your Arduino board to the computer using a USB cable.
Upload the Arduino Code: Compile and upload the code to your board from the Arduino IDE. Close the Arduino IDE after the upload is complete.
Run the Python Code: After adjusting the COM port number to suit your specific board, run the Python file.
## Circuit Connections
* **LDR Sensor**
  *One leg was connected to the + line of the breadboard.
  *The other leg was connected to a 10k resistor and a jumper cable.
  *The tip of the jumper cable was connected to the A0 pin, and the free end of the resistor was connected to the – line.
* **DHT11 Sensor**
  *Signal pin-->D6
  *VCC and GND--> Breadboard + and – lines
* **Buzzer**
  *One leg to the D7 pin.
  *The other leg was connected to the – line.
* **RGB LED Module**
  *R, G, and B pins were connected with 220 ohm resistors respectively.
  *The other ends of the resistors were connected to the D8, D9, and D10 pins.
  *The common cathode of the LED was connected to the – line.
* **Water Level Sensor**
  *Signal pin--> A2
  *VCC and GND--> + and – lines
* **RTC Module**
  *VCC--> +, GND--> –
  *CLK--> D11, DAT--> D12, RST--> D13
* **LCD I2C Screen**
  *SDA-->A4, SCL--> A5
  *VCC and GND--> + and – lines
## Photo of the Circuit
![WhatsApp Image 2025-11-23 at 22 53 04](https://github.com/user-attachments/assets/7653f026-215a-4c65-a8dc-d37eaf84d9a8)
