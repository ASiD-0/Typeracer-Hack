from selenium import webdriver
from time import sleep


def typeracer_hackz():
    driver = webdriver.Chrome(r"C:\Users\ARIS\Downloads\chromedriver.exe")
    driver.get("https://play.typeracer.com/")                                          # Enter the website
    flag_c =False
    flag_text = False                                                                     # Wait for 'Enter Race' Button
    while flag_c == False:
        try:
            driver.find_element_by_xpath('//*[@title="Keyboard shortcut: Ctrl+Alt+I"]').click()  # Presses button to race
            flag_c = True
        except:
            pass

    while flag_text == False:
        try:

            text = driver.find_element_by_class_name("txtInput")                    # Find where to put the text
            print("\nInsert your text in here:\n")
            text.send_keys(input())                                                 # Here is where you insert the copied text
            flag_text = True
        except:
            pass

    while True:                                                                     # RACE AGAIN
        try:
            sleep(2)
            driver.find_element_by_css_selector('button.gwt-Button').click()
            sleep(2)
            driver.find_element_by_css_selector('button.gwt-Button').click()
            sleep(2)
            driver.find_element_by_class_name("xButton").click()
        except:
            pass
        print("\n\n/-----------------------------------\n\n"
              "1) If the text wasn't inserted properly , retry by typing 'Retry'."
              "\n2) If everything went as planned and you want to race again type 'Again'."
              "\n3) To exit the program  type 'Exit'"
              "\n\n/-----------------------------------\n")
        choice = input().casefold()

        if choice == "retry":                                       # IF YOU COPY WRONG THE TEXT RETRY
            try:
                text = driver.find_element_by_class_name("txtInput")
                print("re-Insert your text in here:")
                text.send_keys(input())
            except:
                print("Oops, can't do that anymore")
        elif choice == "again":
            try:
                sleep(2)
                driver.find_element_by_class_name("xButton").click()
            except:
                pass
            driver.find_element_by_class_name("raceAgainLink").click()      # Finds the "Race Again" button
            sleep(5)                                                        # Waits until the text input element appears
            text = driver.find_element_by_class_name("txtInput")            # Find where to put the text
            print("Insert your text in here:")
            text.send_keys(input())                                         # Here is where you insert the copied text
        elif choice == "exit":
            driver.close()
            print("Program exited successfully")
            exit()
        else:
            print("Not recognizable command , please choose again")


typeracer_hackz()
