import time
import plyer

if __name__ == "__main__":
    while True:
         plyer.notification.notify(
           title = "**please drink water NOW !!**",
           message ="The National Academies of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids for men. About 11.5 cups (2.7 liters) of fluids for women",
           timeout= 10)
         time.sleep(60*60)