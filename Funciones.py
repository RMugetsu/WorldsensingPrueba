from datetime import datetime
import wmi

def obtenerTemperaturaCPU():
	w = wmi.WMI(namespace="root\OpenHardwareMonitor")
	Sensores = w.Sensor()
	for sensor in Sensores:
	    if sensor.SensorType==u'Temperature':
	        if sensor.Name=="CPU Package":
	        	return sensor.Value
        	
def escribirRegistroDeLaTemperatura(temperatura):
	f = open("Temperature_Log.txt","a")
	now = datetime.now()
	date = now.strftime("%d/%m/%Y %H:%M:%S")
	texto = str(date)+"--El valor de la temperatura de la cpu es : "+str(temperatura)+"\n"
	f.write(texto)