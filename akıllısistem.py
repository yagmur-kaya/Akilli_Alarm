import serial 
import time 
import pandas as pd 
import matplotlib.pyplot as plt
from datetime import datetime  
import os

try:
    ser_=serial.Serial('COM3',9600,timeout=3)
    print('COM3 portu başarıyla açıldı.')
    time.sleep(2)
except serial.SerialException as port_hatası:
 print(f"Seri porta bağlanılamadı.COM3 portunu kontrol ediniz.{port_hatası}")
 exit();
except PermissionError as permerr_:
 print(f"Port erişimi engellendi.Lütfen kontrol ediniz. {permerr_}")   
 exit();



ldr_value=[]
dht11_value=[]
su_value=[]
saat_modul=[]
alarm_sayısı=[]

tarih_bilgisi=datetime.now().strftime("%Y-%m-%d")
günlük_klasör=f"{tarih_bilgisi}_logs"
if not os.path.exists(günlük_klasör):
    os.makedirs(günlük_klasör)


dosya_yolu=os.path.join(günlük_klasör,"gunluk.csv") 

if not os.path.exists(dosya_yolu):
   with open(dosya_yolu,"w",encoding='utf-8') as file_:
    file_.write("Tarih,Saat,Sıcaklık,LDR,Su,Alarm\n")
print("LDR, Sıcaklık ve Su sensör verileri okunmaya başlandı.")    

num_samples=40
count=0
try:
    while count<num_samples:
        veri=ser_.readline().decode('utf-8',errors='ignore').strip()

        #veri = veri.replace('\r', '').replace('\n', '').strip()
        if not veri:
            continue 
    
        if veri.startswith("Zaman"): #sıcaklıık
         continue
    
        parts = [p.strip() for p in veri.split(",")]   
        if len(parts)!=5:
            print(f"Veri formatı hatalı. Gelen veri:{veri}")
            continue 
        try:
                zaman,dht11_val, ldr_val, su_val, alarm_val = veri.split(",")


                ldr_=int(ldr_val)
                dht11_=float(dht11_val)
                su_=int(su_val)
                alarm_=int(alarm_val)

                current_time=datetime.now()
                tarih=current_time.strftime("%Y-%m-%d")
                saat=current_time.strftime("%H:%M:%S")
                
                ldr_value.append(ldr_)
                dht11_value.append(dht11_)
                su_value.append(su_)
                alarm_sayısı.append(alarm_)
                saat_modul.append(zaman)

                with open(dosya_yolu, "a", encoding="utf-8") as f:
                  f.write(f"{tarih},{saat},{dht11_},{ldr_},{su_},{alarm_}\n")
                print(f"Kayıt: {tarih}  | Sic:{dht11_}°C, LDR:{ldr_}, Su:{su_}, Alarm:{alarm_}")
                count+=1
        except ValueError as value:
               print(f"Uygunsuz değer aldı.{value}")
        except Exception as exc_:
               print(f"Beklenmeyen bir hata oluştu:{exc_}")
               time.sleep(2)
except KeyboardInterrupt:
    print("Veri okuma durduruldu.")
finally:
 if ser_ and ser_.is_open:
  ser_.close()
  print(f"Veri okuma tamamlandı. Seri port kapatıldı.")
  

df=pd.read_csv(dosya_yolu)
print(df.describe())


ort_sıcaklık=df["Sıcaklık"].mean() 
ort_ısık=df["LDR"].mean()
ort_su=df["Su"].mean()

print(f"---Ortalama Sensör Değerleri---")
print(f"Ortalama Sıcaklık: {ort_sıcaklık:.2f}")
print(f"Ortalama Işık: {ort_ısık:.2f}")
print(f"Ortalama Su: {ort_su:.2f}")

Ldr_Esik = 600;    
Su_Esik = 600;
Sıcaklik_Esik = 26.3;

df["Sıcaklık Alarm"]=df["Sıcaklık"]>Sıcaklik_Esik
df["Işık Alarm"]=df["LDR"]<Ldr_Esik
df["Su Alarm"]=df["Su"]>Su_Esik

sıcak_uyarı=df["Sıcaklık Alarm"].sum()
ışık_uyarı=df["Işık Alarm"].sum()
su_uyarı=df["Su Alarm"].sum()

print(f" Sıcaklık Alarmı: {sıcak_uyarı} kez")
print(f"Işık alarmı: {ışık_uyarı} kez")
print(f"Su alarmı: {su_uyarı} kez")

uyarı_df=pd.DataFrame({
   "Alarm Türü": ["Sıcaklık","Işık","Su"],
   "Uyarı Sayısı": [sıcak_uyarı,ışık_uyarı,su_uyarı]
})

#with open(dosya_yolu, "a", encoding='utf-8') as f:
 #  f.writelines(rapor)
  # rapor.clear()

fig,(axs0,axs1,axs2)=plt.subplots(3,1,figsize=(8,10))
fig.suptitle("Sensör Verileri",fontsize=11)

axs0.plot(saat_modul,ldr_value,color="pink",label='LDR')
axs0.set_xticks(range(len(saat_modul))) 
axs0.set_xticklabels(saat_modul, rotation=45, ha='right') 
axs0.set_xlabel("Zaman") 
axs0.set_ylabel("LDR Değeri") 
axs0.legend()


axs1.plot(saat_modul,dht11_value,color="purple",label='DHT11') 
axs1.set_xticks(range(len(saat_modul))) 
axs1.set_xticklabels(saat_modul, rotation=45, ha='right')
axs1.set_xlabel("Zaman") 
axs1.set_ylabel("Sıcaklık Değeri")  
axs1.legend()


axs2.plot(saat_modul,su_value,color="brown",label='Su') 
axs2.set_xticks(range(len(saat_modul))) 
axs2.set_xticklabels(saat_modul, rotation=45, ha='right') 
axs2.set_xlabel("Zaman") 
axs2.set_ylabel("Su Değeri")
axs2.legend()


plt.tight_layout()
plt.show(block=True)

labels=['LDR Alarm','Sıcaklık Alarm','Su Alarm']
sizes=[df["Işık Alarm"].sum(), df["Sıcaklık Alarm"].sum(), df["Su Alarm"].sum()]



fig2,axs3=plt.subplots(figsize=(6,6))
axs3.pie(sizes,labels=labels, colors=["pink","purple","brown"],autopct="%1.1f%%",shadow=True)
axs3.set_title("Alarm Dağılımı")
plt.show()


