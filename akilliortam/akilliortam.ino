#include <LiquidCrystal_I2C.h>
#include "DHT.h"
#include <ThreeWire.h>
#include <RtcDS1302.h>
#include <Wire.h>
#include <math.h>

const int LdrPin = A1;
const int SuSensorPin = A2;
const int BuzzerPin = 7;
const int MaviLedPin = 8;
const int YesilLedPin = 9;
const int KirmiziLedPin = 10;

const int DS1302_IO = 12;  
const int DS1302_SCLK = 11; 
const int DS1302_CE = 13;

ThreeWire myWire(DS1302_IO, DS1302_SCLK, DS1302_CE); 
RtcDS1302<ThreeWire> rtc(myWire);

#define DHTPIN 6
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

LiquidCrystal_I2C lcd(0x27, 16, 2);

const int LdrEsik = 600;
const int SuEsik = 600;
const float SicaklikEsik = 26.3;

void setup() {
  pinMode(LdrPin, INPUT);
  pinMode(SuSensorPin, INPUT);
  pinMode(BuzzerPin, OUTPUT);
  pinMode(MaviLedPin, OUTPUT);
  pinMode(YesilLedPin, OUTPUT);
  pinMode(KirmiziLedPin, OUTPUT);
  noTone(BuzzerPin);

  dht.begin();
  lcd.begin();
  lcd.backlight();
  lcd.setCursor(0, 0);
  lcd.print("Hosgeldiniz!");
  delay(2000);
  lcd.clear();

  Serial.begin(9600);
  Serial.println("Sicaklik,Ldr,Su,Alarm");
  rtc.Begin();


  
  RtcDateTime ayarlananZaman(2025, 10, 17, 16,00, 0); 
  rtc.SetDateTime(ayarlananZaman);
}

void loop() {
  int LdrDeger = analogRead(LdrPin);
  int suDegeri = analogRead(SuSensorPin);
  float sicaklik = dht.readTemperature();

  if (isnan(sicaklik)) {
    Serial.println("HATA: DHT11 verisi okunamadi.");
    delay(2000);
    return;
  }
  RtcDateTime now = rtc.GetDateTime();

  bool SicaklikAlarm = sicaklik > SicaklikEsik;
  bool SuAlarm = suDegeri > SuEsik;
  bool IsikYetersiz = LdrDeger < LdrEsik;

  // LED ve buzzer kontrolü
  if (SicaklikAlarm && SuAlarm && IsikYetersiz) {
    digitalWrite(KirmiziLedPin, HIGH);
    digitalWrite(YesilLedPin, HIGH);
    digitalWrite(MaviLedPin, HIGH);
    tone(BuzzerPin, 2000);
  } else if (SicaklikAlarm && SuAlarm) {
    digitalWrite(KirmiziLedPin, HIGH);
    digitalWrite(YesilLedPin, HIGH);
    digitalWrite(MaviLedPin, LOW);
    tone(BuzzerPin, 1800);
  } else if (SicaklikAlarm && IsikYetersiz) {
    digitalWrite(KirmiziLedPin, HIGH);
    digitalWrite(YesilLedPin, LOW);
    digitalWrite(MaviLedPin, HIGH);
    tone(BuzzerPin, 1600);
  } else if (SuAlarm && IsikYetersiz) {
    digitalWrite(KirmiziLedPin, LOW);
    digitalWrite(YesilLedPin, HIGH);
    digitalWrite(MaviLedPin, HIGH);
    tone(BuzzerPin, 1400);
  } else if (SicaklikAlarm) {
    digitalWrite(KirmiziLedPin, HIGH);
    digitalWrite(YesilLedPin, LOW);
    digitalWrite(MaviLedPin, LOW);
    tone(BuzzerPin, 1000);
  } else if (SuAlarm) {
    digitalWrite(KirmiziLedPin, LOW);
    digitalWrite(YesilLedPin, HIGH);
    digitalWrite(MaviLedPin, LOW);
    tone(BuzzerPin, 1200);
  } else if (IsikYetersiz) {
    digitalWrite(KirmiziLedPin, LOW);
    digitalWrite(YesilLedPin, LOW);
    digitalWrite(MaviLedPin, HIGH);
    tone(BuzzerPin, 1000);
  } else {
    digitalWrite(KirmiziLedPin, LOW);
    digitalWrite(YesilLedPin, LOW);
    digitalWrite(MaviLedPin, LOW);
    noTone(BuzzerPin);
  }
 
 
 static byte oncekiSaniye = 60;  // geçersiz başlangıç
 
 
 if (now.Second() != oncekiSaniye) {
  oncekiSaniye = now.Second();

  char zamanStr[9];
  sprintf(zamanStr, " %02d:%02d:%02d", now.Hour(), now.Minute(), now.Second());

 


  // LCD gösterimi
  lcd.setCursor(0, 0);
  lcd.print("                ");
  lcd.setCursor(0, 0);
  lcd.print("Sic:");
  lcd.print(sicaklik, 1);
  lcd.print(" Ldr:");
  lcd.print(LdrDeger);

  lcd.setCursor(0,1);
  lcd.print("                 ");
  lcd.setCursor(0, 1);
  lcd.print("Su:");
  lcd.print(suDegeri);
  lcd.print(" ");
  lcd.print(zamanStr); 
  lcd.print("                ");
  
  
  

  

  // RTC zamanı gösterimi
                               
  lcd.print(now.Hour());
  lcd.print(":");
  if (now.Minute() < 10) lcd.print("0");
  lcd.print(now.Minute());
  lcd.print(":");
  if (now.Second() < 10) lcd.print("0");
  lcd.print(now.Second());




  int AlarmDurumu = (SicaklikAlarm || SuAlarm || IsikYetersiz) ? 1 : 0;

  //char zamanStr[9];
  sprintf(zamanStr, "%02d:%02d:%02d ", now.Hour(), now.Minute(), now.Second());
  
  Serial.print(zamanStr);
  Serial.print(",");
  Serial.print(sicaklik,2);
  Serial.print(",");
  Serial.print(LdrDeger);
  Serial.print(",");
  Serial.print(suDegeri);
  Serial.print(",");
  Serial.println(AlarmDurumu);

}
}

