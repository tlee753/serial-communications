#include <Wire.h>

#define SLAVE_ADDRESS 0x04 // initialize slave address
int number = 0; // initialize global data value

void setup() {
    Serial.begin(9600); // initialize serial port with baud rate
    Wire.begin(SLAVE_ADDRESS); // initialize slave address

    Wire.onReceive(receiveData); // define callbacks for i2c communication
    Wire.onRequest(sendData);
}

void loop() {
    delay(100); // for stability
}

void receiveData(int byteCount) { // callback for received data
    while(Wire.available()) {
        number = Wire.read();
        Serial.print(“data received: “);
        Serial.println(number);
    }
}

void sendData() { // callback for sending data
    Wire.write(number);
}