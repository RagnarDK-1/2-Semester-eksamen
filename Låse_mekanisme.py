
import RPi.GPIO as GPIO           # Importerer bibliotek til at styre GPIO pins
import mariadb                    # Importerer bibliotek til MariaDB-forbindelse
import time                       # Importerer bibliotek til tidshåndtering

# --- Servo konfiguration ---
SERVO_PIN = 36                   # GPIO16 svarer til fysisk pin 36
GPIO.setmode(GPIO.BOARD)          # Bruger nummering efter boardets fysiske nummerering.
GPIO.setup(SERVO_PIN, GPIO.OUT)  # Sætter servo-pinen som output

# Opsæt PWM signal på servo (50 Hz = standard til servoer)
servo = GPIO.PWM(SERVO_PIN, 50)
servo.start(0)                  # Starter servo med 0% duty cycle (ingen bevægelse)

# --- Databasekonfiguration 
db_config = {
    "user": "admin",             # Brugernavn til MariaDB
    "password": "admin",         # Adgangskode til MariaDB
    "host": "152.115.77.165",    # IP til MariaDB server
    "port": 50110,               # Port MariaDB lytter på
    "database": "motor"         # Navn på databasen
}
# Opret forbindelse til databasen og aktiver autocommit
# autocommit=True betyder at alle ændringer (INSERT, UPDATE osv.) automatisk gemmes uden at kalde conn.commit()
conn = mariadb.connect(**db_config, autocommit=True)
cursor = conn.cursor()

try:
    last_status = None #Husker tidliger status hjælper med at forhindre spam
    while True:
        cursor.execute("SELECT status FROM motor_kontrol WHERE id=1")  # Henter status-værdi
        status = cursor.fetchone()[0]  # Gemmer værdien (0 eller 1)

        if status != last_status: # != not equal to, altså hvis statusen ikke er det samme som "last_status" så kører if
            if status == 1:
                print("-Låser op-")
                servo.ChangeDutyCycle(12.5)  # Ca. 180 grader
            else:
                print("-Låser-")
                servo.ChangeDutyCycle(2.5)   # Ca. 0 grader

        time.sleep(1)  # Venter 1 sekund før næste check

except mariadb.Error as e: # ved fejl af mariadb udskriver den "database fejl"
    print(f"Databasefejl: {e}")
except KeyboardInterrupt: # ved CTRL+C skriver den afslutter script
    print("Afslutter script")
finally:
    servo.stop()           # Stopper PWM signal
    GPIO.cleanup()         # Nulstiller alle GPIO-pins
