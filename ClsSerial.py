import serial
import threading, time
import serial.tools.list_ports
import sys
import glob

class SerialComm:
    
    def __init__(self):
        self.port = 'COM3'
        self.baudrate = 115200
        self.parity = serial.PARITY_NONE
        self.stopBits = serial.STOPBITS_ONE
        self.DataBits = serial.EIGHTBITS
        
        self.ser = serial.Serial(self.port,self.baudrate, timeout=1)
        self.PortOpen()
        #self.thread = threading.Thread(target=self.ReadSerial, args=(self.ser,))
        #self.thread.start()
        self.ReadStart = False
        self.WriteStart = False
        
    def ReadSerial(self):
        
        if self.Port_IsOpen:
            
            self.ReadStart = True
            
            while self.ReadStart:
                if self.ser.readable():
                    #res = self.ser.readline().decode("ascii").strip()
                    res = self.ser.readline()
                    print(res)
                    res = b'abcdefghidsada'
                    self.ser.write(res)
                    print(res)
                    
            time.sleep(1000)
            
            
                    
        else:
            
            self.threadSwitch = False
            print("Port Connect Fail")
            
    
    def WriteSerial(self,data):
        
        try:
            if self.PortIsOpen():
                self.ser.write(data)
            else:
                print("port Open Fail")
        except:
            
            self.portClose()
            print("Write Fail")
             
    def WriteEncodeSerial(self, data):
        
        pass
    
    def PortOpen(self):
        
        try:
            
            if self.ser.is_open:
                
                self.ser.close()    
                self.ser.open()
            else:
                
                self.ser.open()
            
        except:
            print("Port Open Fail")
            
    def Port_IsOpen(self):
        
       res =  self.ser.isOpen
       return res
   
    def portClose(self):
        
        self.ser.close()
        
            
if __name__ == "__main__":
    seri = SerialComm()
    #seri.thread.start()
    seri.ReadSerial()
   