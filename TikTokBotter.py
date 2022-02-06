import time, sys, os, colorama
from colorama import Fore
from selenium import webdriver
#gig
#gig

def type(str, wait):
  for letter in str:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(wait)
  print()

os.system("title TikTok Botter -By Dreamer#5114")
indentLines = int(round(os.get_terminal_size().lines/2))
print("\n" * indentLines)
print(f"""
{Fore.LIGHTMAGENTA_EX}     
{" "*round(os.get_terminal_size().columns/2-19)}      _                                 
{" "*round(os.get_terminal_size().columns/2-19)} ___/__)        /) ,                    
{" "*round(os.get_terminal_size().columns/2-19)}(, /   ____   _(/   __   _              
{" "*round(os.get_terminal_size().columns/2-19)}  /   (_)(_(_(_(__(_/ (_(_/_{Fore.LIGHTGREEN_EX} o   o   o{Fore.LIGHTMAGENTA_EX}
{" "*round(os.get_terminal_size().columns/2-19)} (_____                .-/              
{" "*round(os.get_terminal_size().columns/2-19)}        )             (_/               \n\n
""")
print(f"{' ' * round(os.get_terminal_size().columns/2-21)}\t{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}]{Fore.LIGHTGREEN_EX} TIP: {Fore.LIGHTMAGENTA_EX}Not Loading? Press Enter.")
print("\n" * indentLines)

def printBigText():
    bigText1 = f"""
{Fore.LIGHTMAGENTA_EX}
{" "*round(os.get_terminal_size().columns/2-32)}▄▄▄▄▄▪  ▄ •▄ ▄▄▄▄▄      ▄ •▄     ▄▄▄▄·       ▄▄▄▄▄▄▄▄▄▄▄▄▄ .▄▄▄  
{" "*round(os.get_terminal_size().columns/2-32)} ██  ██ █▌▄▌▪•██  ▪     █▌▄▌▪    ▐█ ▀█▪▪     •██  •██  ▀▄.▀·▀▄ █·
{" "*round(os.get_terminal_size().columns/2-32)} ▐█.▪▐█·▐▀▀▄· ▐█.▪ ▄█▀▄ ▐▀▀▄·    ▐█▀▀█▄ ▄█▀▄  ▐█.▪ ▐█.▪▐▀▀▪▄▐▀▀▄ 
{" "*round(os.get_terminal_size().columns/2-32)} ▐█▌·▐█▌▐█.█▌ ▐█▌·▐█▌.▐▌▐█.█▌    ██▄▪▐█▐█▌.▐▌ ▐█▌· ▐█▌·▐█▄▄▌▐█•█▌
{" "*round(os.get_terminal_size().columns/2-32)} ▀▀▀ ▀▀▀·▀  ▀ ▀▀▀  ▀█▄▀▪·▀  ▀    ·▀▀▀▀  ▀█▄▀▪ ▀▀▀  ▀▀▀  ▀▀▀ .▀  ▀
"""
    bigText2 = bigText1.replace('▪', f'{Fore.GREEN}▪{Fore.LIGHTMAGENTA_EX}')
    bigText3 = bigText2.replace('•', f'{Fore.GREEN}•{Fore.LIGHTMAGENTA_EX}')
    bigText4 = bigText3.replace('·', f'{Fore.GREEN}·{Fore.LIGHTMAGENTA_EX}')
    bigText5 = bigText4.replace('.', f'{Fore.GREEN}.{Fore.LIGHTMAGENTA_EX}')
    print(bigText5)

def printOptions():
    options = f"""
    {Fore.WHITE}
{" "*round(os.get_terminal_size().columns/2-16)}╔═══════════════════════════════╗
{" "*round(os.get_terminal_size().columns/2-16)}║                               ║
{" "*round(os.get_terminal_size().columns/2-16)}║          {Fore.WHITE}[{Fore.LIGHTGREEN_EX}1{Fore.WHITE}] {Fore.LIGHTMAGENTA_EX}Start{Fore.WHITE}            ║
{" "*round(os.get_terminal_size().columns/2-16)}║          {Fore.WHITE}[{Fore.LIGHTGREEN_EX}2{Fore.WHITE}] {Fore.LIGHTMAGENTA_EX}Info{Fore.WHITE}             ║
{" "*round(os.get_terminal_size().columns/2-16)}║          {Fore.WHITE}[{Fore.LIGHTGREEN_EX}3{Fore.WHITE}] {Fore.LIGHTMAGENTA_EX}Options{Fore.WHITE}          ║
{" "*round(os.get_terminal_size().columns/2-16)}║          {Fore.WHITE}[{Fore.LIGHTGREEN_EX}4{Fore.WHITE}] {Fore.LIGHTMAGENTA_EX}Clear/Refresh{Fore.WHITE}    ║
{" "*round(os.get_terminal_size().columns/2-16)}║          {Fore.WHITE}[{Fore.LIGHTGREEN_EX}5{Fore.WHITE}] {Fore.LIGHTMAGENTA_EX}Exit{Fore.WHITE}             ║
{" "*round(os.get_terminal_size().columns/2-16)}║                               ║
{" "*round(os.get_terminal_size().columns/2-16)}╚═══════════════════════════════╝
    """
    print(options)

def printInfo():
    info = f"""
{Fore.WHITE}
{" "*round(os.get_terminal_size().columns/2-42)}╔═══════════════════════════════════════════════════════════════════════════════════╗
{" "*round(os.get_terminal_size().columns/2-42)}║                                                                                   ║
{" "*round(os.get_terminal_size().columns/2-42)}║          {Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}About: {Fore.LIGHTMAGENTA_EX}This Is A Advanced Tool That Uses Zefoy{Fore.WHITE}                       ║
{" "*round(os.get_terminal_size().columns/2-42)}║                     {Fore.LIGHTMAGENTA_EX}To Bot TikTok Follows, Hearts, Views, & Shares.{Fore.WHITE}               ║
{" "*round(os.get_terminal_size().columns/2-42)}║          {Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Updates: {Fore.LIGHTMAGENTA_EX}Minor Adjustments --1/28/2022{Fore.WHITE}                               ║
{" "*round(os.get_terminal_size().columns/2-42)}║          {Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Made By: {Fore.LIGHTMAGENTA_EX}Dreamer#5114{Fore.WHITE}                                                ║
{" "*round(os.get_terminal_size().columns/2-42)}║          {Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Github: {Fore.LIGHTMAGENTA_EX}https://github.com/OriginalAlien{Fore.WHITE}                             ║
{" "*round(os.get_terminal_size().columns/2-42)}║          {Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Download Chrome Driver: {Fore.LIGHTMAGENTA_EX}https://chromedriver.chromium.org/downloads{Fore.WHITE}  ║
{" "*round(os.get_terminal_size().columns/2-42)}║                                                                                   ║
{" "*round(os.get_terminal_size().columns/2-42)}╚═══════════════════════════════════════════════════════════════════════════════════╝
"""
    print(info)

def clear():
    os.system("cls")

    printBigText()

    print(f'{" "*round(os.get_terminal_size().columns/2-14)}{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Made By: {Fore.LIGHTMAGENTA_EX}Dreamer#5114 {Fore.WHITE}[{Fore.LIGHTGREEN_EX}<{Fore.WHITE}]\n{" "*round(os.get_terminal_size().columns/2-30)}{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Github: {Fore.LIGHTMAGENTA_EX}https://github.com/OriginalAlien/TikTokBotter {Fore.WHITE}[{Fore.LIGHTGREEN_EX}<{Fore.WHITE}]')

    printOptions()

def start():
    type(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Note: {Fore.LIGHTGREEN_EX}Please Make Sure It's An Actual Valid TikTok Link, It Can Cause Errors Later If Not.", wait = 0.01)
    video_url = input(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>>>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Video URL: {Fore.LIGHTMAGENTA_EX}")

    while "tiktok" not in video_url:
        type(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}Please Enter A Valid Link.", 0.01)
        video_url = input(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>>>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Video URL: {Fore.LIGHTMAGENTA_EX}")
        if "tiktok" in video_url:
            type(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Opening Chrome Web Driver...\n", 0.01)
            break

    main(video_url)


def main(url):
    option = webdriver.ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-logging'])
    try:
        driver = webdriver.Chrome("Chrome Driver Path, Example: C:\\USERS\\User\\OneDrive\\Desktop\\Chromedriver\\chromedriver.exe", options=option) #Put chromedriver.exe file loction between quotation marks using double back slashes.
    except Exception as DriverError:
        type(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}Invalid File Location For Chrome Driver Or File Location Hasn't Been Set Yet. Remember To Use Double Slashes. Or Chrome Driver Version Isn't The Same As Chrome. (Make Sure You Delete The Chrome Driver Path Text, Example Before The File Location)\n{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}Line: 102\n{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}Stopped Program.\n", 0.01)
        print(f"{DriverError}{Fore.RESET}\n")
        time.sleep(7)
        exit()
    driver.set_window_size(777, 777)
    driver.get('https://zefoy.com')
    amount = 0

    if driver.title == "zefoy.com | 502: Bad gateway":
                type(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}Zefoy Is Down... Attempting To Fix.\n")
                while driver.title == "zefoy.com | 502: Bad gateway":
                    time.sleep(20)
                    driver.refresh()
                    if driver.title != "zefoy.com | 502: Bad gateway":
                        type(f"{Fore.LIGHTGREEN_EX}\nFixed! Zefoy is Back Up. Starting Now.\n", 0.01)
                        break
    else:
        pass
        type(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Zefoy Is Up!{Fore.WHITE}\n", 0.01)


    type(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Type \"y\" Once You Finished Captcha.", 0.01)
    captcha_finish = input(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>>>{Fore.WHITE}] {Fore.GREEN}{Fore.LIGHTMAGENTA_EX}")
    if captcha_finish == "y":
        while captcha_finish != True:
            try:
                driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[1]/div/h5")
                captcha_finish = True
            except:
                type(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}You Didn't Finish The Captcha.", 0.01)
                captcha_finish = False
                type(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Type \"y\" Once You Finished Captcha.", 0.01)
                captcha_finish = input(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>>>{Fore.WHITE}] {Fore.GREEN}{Fore.LIGHTMAGENTA_EX}")
                if captcha_finish == True:
                    break
    
    while captcha_finish == True:
        type(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Captcha Is Solved, Starting Now!", 0.01)

        follows_cooldown = 0
        hearts_cooldown = 0
        views_cooldown = 0
        shares_cooldown = 0
        Follow_Seconds = 0
        Follow_Minutes = 0
        Heart_Seconds = 0
        Heart_Minutes = 0
        View_Minutes = 0
        View_Seconds = 0
        Share_Minutes = 0
        Share_Seconds = 0
        Follow_Continue1 = False
        Follow_Continue2 = False
        Heart_Continue1 = False
        Heart_Continue2 = False
        View_Continue1 = False
        View_Continue2 = False
        Share_Continue1 = False
        Share_Continue2 = False

        while captcha_finish == True:
            if driver.title == "zefoy.com | 502: Bad gateway":
                type(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}]{Fore.LIGHTRED_EX}\nZefoy Is Down... Attempting To Fix.\n", 0.01)
                while driver.title == "zefoy.com | 502: Bad gateway":
                    time.sleep(20)
                    driver.refresh()
                    if driver.title != "zefoy.com | 502: Bad gateway":
                        type(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX} Fixed! Zefoy is Back Up. Starting Now.\n", 0.01)
                        break
            else:
                type(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Zefoy Is Up.{Fore.WHITE}\n", 0.01)
                pass
            
            try:
                try:
                    #Follows
                    driver.find_element_by_xpath('/html/body/nav/ul/li/a').click()
                    follows_cooldown = 0

                    try:
                        driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/div/button').click()
                        driver.find_element_by_xpath('//*[@id="sid"]/div/form/div/input').send_keys(url)
                        Follow_Continue1 = True
                    except:
                        type(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}Follower Send Page Is Down.\n{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}Skipping...{Fore.WHITE}\n", 0.01)
                        Follow_Continue1 = False
                        Follow_Seconds = 0
                        Follow_Minutes = 0
                        follows_cooldown = 0

                    if Follow_Continue1 == True:
                        driver.find_element_by_xpath('//*[@id="sid"]/div/form/div/div/button').click()
                        time.sleep(3)
                        try:
                            driver.find_element_by_xpath('//*[@id="c2VuZF9mb2xsb3dlcnNfdGlrdG9r"]/div[1]/div/form/button').click()
                            Follow_Continue2 = True
                        except:
                            type(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}Follow Cool Down Isn't Finished Yet. Getting Cool Down And Skipping...\n {Fore.WHITE}", 0.01)
                            Follow_Continue2 = False
                            Follow_Text = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div/h4").text
                            time.sleep(3)

                            if Follow_Text[13] == " ":
                                Follow_Minutes = int(Follow_Text[12])
                                Follow_Seconds = Follow_Minutes * 60

                            elif Follow_Text[13] != " ":
                                Follow_Minutes = int(Follow_Text[12:14])
                                Follow_Seconds = Follow_Minutes * 60

                            if Follow_Text[24] == "0":
                                Follow_Seconds += int(Follow_Text[25])
                            elif Follow_Text[24] != "0":
                                Follow_Seconds += int(Follow_Text[24:26])

                            Follow_Seconds += 5
                            follows_cooldown += Follow_Seconds

                            type(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Follow Cool Down: {Fore.LIGHTCYAN_EX}{Follow_Minutes}{Fore.LIGHTMAGENTA_EX} Minutes And {Fore.LIGHTCYAN_EX}{Follow_Seconds%60}{Fore.LIGHTMAGENTA_EX} Seconds.\n", 0.01)

                        if Follow_Continue2 == True:
                            type(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}\nSent Followers!\n{Fore.WHITE}\n", 0.01)
                            type(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Getting Cool Down...{Fore.WHITE}\n", 0.01)
                            time.sleep(10)
                            Follow_Text = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/h4').text

                            try:
                                if Follow_Text[13] == " ":
                                    Follow_Minutes = int(Follow_Text[12])
                                    Follow_Seconds = Follow_Minutes * 60

                                elif Follow_Text[13] != " ":
                                    Follow_Minutes = int(Follow_Text[12:14])
                                    Follow_Seconds = Follow_Minutes * 60

                                if Follow_Text[24] == "0":
                                    Follow_Seconds += int(Follow_Text[25])
                                elif Follow_Text[24] != "0":
                                    Follow_Seconds += int(Follow_Text[24:26])

                                Follow_Seconds += 5
                                follows_cooldown += Follow_Seconds
                            except:
                                type(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}An Error Occurred When Attempting To Get Follow's Cool Down. (Skipping){Fore.WHITE}\n", 0.01)
                                Follow_Minutes = 0
                                Follow_Seconds = 0
                                follows_cooldown = 0


                            type(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Follow Cool Down:{Fore.LIGHTCYAN_EX}{Follow_Minutes}{Fore.LIGHTMAGENTA_EX} Minutes And {Fore.LIGHTCYAN_EX}{Follow_Seconds%60}{Fore.LIGHTMAGENTA_EX} Seconds.{Fore.WHITE}\n", 0.01)

                        else:
                            pass
                    else:
                        pass

                except Exception as Follows_Error:
                    type(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}Error Occurred When Attempting To Send Follows.\n{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}Error: {Follows_Error}{Fore.WHITE}\n", 0.01)
                    driver.find_element_by_xpath('/html/body/nav/ul/li/a').click()
                    Follow_Minutes = 0
                    Follow_Seconds = 0
                    follows_cooldown = 0


                try:
                    #Views
                    driver.refresh()
                    try:
                        driver.find_element_by_xpath('//*[@id="main"]/div/div[4]/div/button').click()
                        driver.find_element_by_xpath('//*[@id="sid4"]/div/form/div/input').send_keys(url)
                        View_Continue1 = True
                    except:
                        type(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}Views Send Page Is Down.\n{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}Skipping...{Fore.WHITE}\n", 0.01)
                        View_Continue1 = False
                        View_Seconds = 0
                        View_Minutes = 0
                        views_cooldown = 0

                    if View_Continue1 == True:
                        driver.find_element_by_xpath('//*[@id="sid4"]/div/form/div/div/button').click()
                        time.sleep(2)

                        driver.refresh()
                        time.sleep(0.7)
                        driver.find_element_by_xpath('//*[@id="main"]/div/div[4]/div/button').click()
                        driver.find_element_by_xpath('//*[@id="sid4"]/div/form/div/input').send_keys(url)
                        driver.find_element_by_xpath('//*[@id="sid4"]/div/form/div/div/button').click()
                        time.sleep(3)
                        try:
                            driver.find_element_by_xpath('/html/body/div[4]/div[5]/div/div/div[1]/div/form/button').click()
                            View_Continue2 = True
                        except:
                            View_Continue2 = False
                            View_Text = driver.find_element_by_xpath("/html/body/div[4]/div[5]/div/div/h4").text
                            type(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}View Cool Down Isn't Finished Yet. Getting Cool Down And Skipping...\n {Fore.WHITE}", 0.01)
                            time.sleep(3)

                            if View_Text[13] == " ":
                                View_Minutes = int(View_Text[12])
                                View_Seconds = View_Minutes * 60

                            elif View_Text[13] != " ":
                                View_Minutes = int(View_Text[12:14])
                                View_Seconds = View_Minutes * 60

                            if View_Text[24] == "0":
                                View_Seconds += int(View_Text[25])
                            elif View_Text[24] != "0":
                                View_Seconds += int(View_Text[24:26])

                            View_Seconds += 5
                            views_cooldown += View_Seconds

                            type(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}View Cool Down: {Fore.LIGHTCYAN_EX}{View_Minutes}{Fore.LIGHTMAGENTA_EX} Minutes And {Fore.LIGHTCYAN_EX}{View_Seconds%60}{Fore.LIGHTMAGENTA_EX} Seconds.{Fore.WHITE}\n", 0.01)
                            driver.refresh()

                        if View_Continue2 == True:
                            type(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Sent Views!\n{Fore.WHITE}", 0.01)
                            type(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Getting Cool Down...{Fore.WHITE}\n", 0.01)
                            time.sleep(10)

                            View_Text = driver.find_element_by_xpath("/html/body/div[4]/div[5]/div/div/h4").text

                            try:
                                if View_Text[13] == " ":
                                    View_Minutes = int(View_Text[12])
                                    View_Seconds = View_Minutes * 60

                                elif View_Text[13] != " ":
                                    View_Minutes = int(View_Text[12:14])
                                    View_Seconds = View_Minutes * 60

                                if View_Text[24] == "0":
                                    View_Seconds += int(View_Text[25])
                                elif View_Text[24] != "0":
                                    View_Seconds += int(View_Text[24:26])

                                View_Seconds += 5
                                views_cooldown += View_Seconds
                                
                            except:
                                type(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}An Error Occurred When Attempting To Get View's Cool Down. (Skipping){Fore.WHITE}\n", 0.01)
                                View_Minutes = 0
                                View_Seconds = 0
                                views_cooldown = 0

                            type(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}View Cool Down: {Fore.LIGHTCYAN_EX}{View_Minutes}{Fore.LIGHTMAGENTA_EX} Minutes And {Fore.LIGHTCYAN_EX}{View_Seconds%60}{Fore.LIGHTMAGENTA_EX} Seconds.{Fore.WHITE}\n", 0.01)

                        else:
                            pass

                    else:
                        pass
                        
                except Exception as Views_Error:
                    type(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}Error Occurred When Attempting To Send Views.\n{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}Error: {Views_Error}{Fore.WHITE}\n", 0.01)
                    driver.find_element_by_xpath('/html/body/nav/ul/li/a').click()
                    View_Minutes = 0
                    View_Seconds = 0
                    views_cooldown = 0
                

                try:
                    #Hearts
                    driver.find_element_by_xpath('/html/body/nav/ul/li/a').click()
                    hearts_cooldown = 0

                    try:
                        driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/button').click()
                        driver.find_element_by_xpath('//*[@id="sid2"]/div/form/div/input').send_keys(url)
                        Heart_Continue1 = True
                    except:
                        type(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}Heart Send Page Is Down.\n{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}Skipping...{Fore.WHITE}\n", 0.01)
                        Heart_Continue1 = False
                        Heart_Seconds = 0
                        Heart_Minutes = 0
                        hearts_cooldown = 0

                    if Heart_Continue1 == True:
                        driver.find_element_by_xpath('//*[@id="sid2"]/div/form/div/div/button').click()
                        time.sleep(3)
                        try:
                            driver.find_element_by_xpath('//*[@id="c2VuZE9nb2xsb3dlcnNfdGlrdG9r"]/div[1]/div/form/button').click()
                            Heart_Continue2 = True

                        except:
                            type(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}Heart Cool Down Isn't Finished Yet. Getting Cool Down And Skipping...\n {Fore.WHITE}", 0.01)
                            Heart_Continue2 = False
                            Heart_Text = driver.find_element_by_xpath("/html/body/div[4]/div[3]/div/div/h4").text
                            time.sleep(3)

                            if Heart_Text[13] == " ":
                                Heart_Minutes = int(Heart_Text[12])
                                Heart_Seconds = Heart_Minutes * 60

                            elif Heart_Text[13] != " ":
                                Heart_Minutes = int(Heart_Text[12:14])
                                Heart_Seconds = Heart_Minutes * 60

                            if Heart_Text[24] == "0":
                                Heart_Seconds += int(Heart_Text[25])
                            elif Heart_Text[24] != "0":
                                Heart_Seconds += int(Heart_Text[24:26])

                            Heart_Seconds += 7
                            hearts_cooldown += Heart_Seconds

                            type(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Heart Cool Down: {Fore.LIGHTCYAN_EX}{Heart_Minutes}{Fore.LIGHTMAGENTA_EX} Minutes And {Fore.LIGHTCYAN_EX}{Heart_Seconds%60}{Fore.LIGHTMAGENTA_EX} Seconds.{Fore.WHITE}\n", 0.01)

                        if Heart_Continue2 == True:
                            type(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Sent Hearts!\n{Fore.WHITE}\n", 0.01)
                            type(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Getting Cool Down...{Fore.WHITE}\n", 0.01)
                            time.sleep(10)

                            Heart_Text = driver.find_element_by_xpath("/html/body/div[4]/div[3]/div/div/h4").text #Finding the cooldown for the heart's xpath is for some reason inaccurate.

                            try:
                                if Heart_Text[13] == " ":
                                    Heart_Minutes = int(Heart_Text[12])
                                    Heart_Seconds = Heart_Minutes * 60

                                elif Heart_Text[13] != " ":
                                    Heart_Minutes = int(Heart_Text[12:14])
                                    Heart_Seconds = Heart_Minutes * 60

                                if Heart_Text[24] == "0":
                                    Heart_Seconds += int(Heart_Text[25])
                                elif Heart_Text[24] != "0":
                                    Heart_Seconds += int(Heart_Text[24:26])

                                Heart_Seconds += 5
                                hearts_cooldown += Heart_Seconds
                            except:
                                type(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}An Error Occurred When Attempting To Get Heart's Cool Down. (Skipping){Fore.WHITE}\n", 0.01)
                                Heart_Minutes = 0
                                Heart_Seconds = 0
                                hearts_cooldown = 0

                            type(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Heart Cool Down: {Fore.LIGHTCYAN_EX}{Heart_Minutes}{Fore.LIGHTMAGENTA_EX} Minutes And {Fore.LIGHTCYAN_EX}{Heart_Seconds%60}{Fore.LIGHTMAGENTA_EX} Seconds.{Fore.WHITE}\n", 0.01)

                            driver.refresh()
                        else:
                            pass
                    else:
                        pass
                    
                except Exception as Hearts_Error:
                    type(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}Error Occurred When Attempting To Send Hearts.\n{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}Error: {Hearts_Error}{Fore.WHITE}\n", 0.01)
                    Heart_Minutes = 0
                    Heart_Seconds = 0
                    hearts_cooldown = 0

                try:
                    #Shares
                    driver.find_element_by_xpath('/html/body/nav/ul/li/a').click()
                    try:
                        driver.find_element_by_xpath('//*[@id="main"]/div/div[5]/div/button').click()
                        driver.find_element_by_xpath('//*[@id="sid7"]/div/form/div/input').send_keys(url)
                        Share_Continue1 = True
                    except:
                        Share_Continue1 = False
                        type(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.RED}Share Send Page Is Down.\n{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}Skipping...\n{Fore.WHITE}", 0.01)
                        Share_Minutes = 0
                        Share_Seconds = 0
                        shares_cooldown = 0

                    if Share_Continue1 == True:
                        driver.find_element_by_xpath('//*[@id="sid7"]/div/form/div/div/button').click()
                        time.sleep(3)
                        try:
                            driver.find_element_by_xpath('//*[@id="c2VuZC9mb2xsb3dlcnNfdGlrdG9s"]/div[1]/div/form/button').click()
                            Share_Continue2 = True
                        except:
                            Share_Continue2 = False
                            type(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}Share Cool Down Isn't Finished Yet. Getting Cool Down And Skipping...\n {Fore.WHITE}", 0.01)
                            Share_Text = driver.find_element_by_xpath('/html/body/div[4]/div[6]/div/div/h4').text
                            time.sleep(3)

                            if Share_Text[13] == " ":
                                Share_Minutes = int(Share_Text[12])
                                Share_Seconds = Share_Minutes * 60

                            elif Share_Text[13] != " ":
                                Share_Minutes = int(Share_Text[12:14])
                                Share_Seconds = Share_Minutes * 60

                            if Share_Text[24] == "0":
                                Share_Seconds += int(Share_Text[25])
                            elif Share_Text[24] != "0":
                                Share_Seconds += int(Share_Text[24:26])

                            Share_Seconds += 5
                            shares_cooldown += Share_Seconds

                            type(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Share Cool Down: {Fore.LIGHTCYAN_EX}{Share_Minutes}{Fore.LIGHTMAGENTA_EX} Minutes And {Fore.LIGHTCYAN_EX}{Share_Seconds%60}{Fore.LIGHTMAGENTA_EX} Seconds.{Fore.WHITE}\n", 0.01)
                            driver.find_element_by_xpath('/html/body/nav/ul/li/a').click()

                        if Share_Continue2 == True:
                            type(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Sent Shares!\n{Fore.WHITE}", 0.01)
                            type(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Getting Cool Down...{Fore.WHITE}\n", 0.01)
                            time.sleep(10)
                            Share_Text = driver.find_element_by_xpath('/html/body/div[4]/div[6]/div/div/h4').text

                            try:
                                if Share_Text[13] == " ":
                                    Share_Minutes = int(Share_Text[12])
                                    Share_Seconds = Share_Minutes * 60

                                elif Share_Text[13] != " ":
                                    Share_Minutes = int(Share_Text[12:14])
                                    Share_Seconds = Share_Minutes * 60

                                if Share_Text[24] == "0":
                                    Share_Seconds += int(Share_Text[25])
                                elif Share_Text[24] != "0":
                                    Share_Seconds += int(Share_Text[24:26])

                                Share_Seconds += 5
                                shares_cooldown += Share_Seconds
                            except:
                                type(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}An Error Occurred When Attempting To Get Share's Cool Down. (Skipping){Fore.WHITE}\n", 0.01)
                                Share_Minutes = 0
                                Share_Seconds = 0
                                shares_cooldown = 0

                            type(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Share Cool Down: {Fore.LIGHTCYAN_EX}{Share_Minutes}{Fore.LIGHTMAGENTA_EX} Minutes And {Fore.LIGHTCYAN_EX}{Share_Seconds%60}{Fore.LIGHTMAGENTA_EX} Seconds.{Fore.WHITE}\n", 0.01)

                except Exception as Shares_Error:
                    type(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}Error Occurred When Attempting To Send Shares.\n{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}Error: {Shares_Error}{Fore.WHITE}\n", 0.01)
                    Share_Minutes = 0
                    Share_Seconds = 0
                    shares_cooldown = 0
                    driver.find_element_by_xpath('/html/body/nav/ul/li/a').click()

            except Exception as AllError:
                type(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}An Error Occured When Trying To Send Followers, Hearts, Views, & Shares.\n{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}Most Likely Zefoy Is Down, Attempting To Troubleshoot.\n", 0.01)
                if driver.title == "zefoy.com | 502: Bad gateway":
                    type(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}Zefoy Is Down... Attempting To Fix.\n", 0.01)
                    while driver.title == "zefoy.com | 502: Bad gateway":
                        time.sleep(20)
                        driver.refresh()
                        if driver.title != "zefoy.com | 502: Bad gateway":
                            type(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Fixed! Zefoy is Back Up.\n", 0.01)
                            break
                else:
                    type(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}Couldn't Fix The Problem. Maybe It's Your Internet?\n{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}Error: {AllError}\n\n{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}Exitted Program.{Fore.WHITE}\n", 0.01)
                    time.sleep(7)
                    exit()

            driver.find_element_by_xpath('/html/body/nav/ul/li/a').click()
            amount += 1
            type(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.GREEN}Sent Followers, Hearts, Views, & Shares {amount} Times.{Fore.WHITE}", 0.01)

            LargestCoolDown = [follows_cooldown, hearts_cooldown, views_cooldown, shares_cooldown]
            LargestCoolDown.sort()
            AntiAFKTime = int(LargestCoolDown[-1]) + 60
            AntiAFKTime /= 5

            Follow_Spaces = 85 - (len(f'{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTMAGENTA_EX}Follow: {Fore.LIGHTCYAN_EX}{Follow_Minutes}m, {follows_cooldown%60}s ({follows_cooldown}s){Fore.WHITE}') - 13)
            Heart_Spaces = 85 - (len(f'{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Hearts: {Fore.LIGHTCYAN_EX}{Heart_Minutes}m, {hearts_cooldown%60}s ({hearts_cooldown}s){Fore.WHITE}') - 13)
            View_Spaces = 85 - (len(f'{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Views: {Fore.LIGHTCYAN_EX}{View_Minutes}m, {views_cooldown%60}s ({views_cooldown}s){Fore.WHITE}') - 13)
            Share_Spaces = 85 - (len(f'{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Shares: {Fore.LIGHTCYAN_EX}{Share_Minutes}m, {shares_cooldown%60}s ({shares_cooldown}s){Fore.WHITE}') - 13)
            AntiAFK_Spaces = 85 - (len(f'{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Seconds Before Refreshing 5x: {Fore.LIGHTCYAN_EX}{AntiAFKTime}{Fore.WHITE}') - 13)

            print(f"""
{" "*round(os.get_terminal_size().columns/2-42)}╔═════════════════════════════════════════════════════════════════════════╗
{" "*round(os.get_terminal_size().columns/2-42)}║                               {Fore.LIGHTGREEN_EX}Cool Downs{Fore.WHITE}                                ║
{" "*round(os.get_terminal_size().columns/2-42)}║                                                                         ║
{" "*round(os.get_terminal_size().columns/2-42)}║     {Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTMAGENTA_EX}Follow: {Fore.LIGHTCYAN_EX}{Follow_Minutes}m, {follows_cooldown%60}s ({follows_cooldown}s){Fore.WHITE}{Follow_Spaces*' '}║
{" "*round(os.get_terminal_size().columns/2-42)}║     {Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTMAGENTA_EX}Hearts: {Fore.LIGHTCYAN_EX}{Heart_Minutes}m, {hearts_cooldown%60}s ({hearts_cooldown}s){Fore.WHITE}{Heart_Spaces*' '}║
{" "*round(os.get_terminal_size().columns/2-42)}║     {Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTMAGENTA_EX}Views: {Fore.LIGHTCYAN_EX}{View_Minutes}m, {views_cooldown%60}s ({views_cooldown}s){Fore.WHITE}{View_Spaces*' '}║
{" "*round(os.get_terminal_size().columns/2-42)}║     {Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTMAGENTA_EX}Shares: {Fore.LIGHTCYAN_EX}{Share_Minutes}m, {shares_cooldown%60}s ({shares_cooldown}s){Fore.WHITE}{Share_Spaces*' '}║
{" "*round(os.get_terminal_size().columns/2-42)}║     {Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTMAGENTA_EX}Seconds Before Refreshing 5x: {Fore.LIGHTCYAN_EX}{AntiAFKTime}{Fore.WHITE}{AntiAFK_Spaces*' '}║
{" "*round(os.get_terminal_size().columns/2-42)}║                                                                         ║
{" "*round(os.get_terminal_size().columns/2-42)}╚═════════════════════════════════════════════════════════════════════════╝
""")
            type(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Reminder: {Fore.LIGHTMAGENTA_EX}Please Do Not Interact With The Tabs In Chrome Web Driver As It Can Mess Up The Code And Give Errors", 0.01)

            time.sleep(AntiAFKTime)
            driver.refresh()
            type(f"\n{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Refreshed Zefoy To Prevent Session From Expiring. {Fore.LIGHTCYAN_EX}(1/5 Cool Down){Fore.WHITE}\n", 0.01)

            time.sleep(AntiAFKTime)
            driver.refresh()
            type(f"\n{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Refreshed Zefoy To Prevent Session From Expiring. {Fore.LIGHTCYAN_EX}(2/5 Cool Down){Fore.WHITE}\n", 0.01)

            time.sleep(AntiAFKTime)
            driver.refresh()
            type(f"\n{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Refreshed Zefoy To Prevent Session From Expiring {Fore.LIGHTCYAN_EX}(3/5 Cool Down){Fore.WHITE}\n", 0.01)

            time.sleep(AntiAFKTime)
            driver.refresh()
            type(f"\n{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Refreshed Zefoy To Prevent Session From Expiring {Fore.LIGHTCYAN_EX}(4/5 Cool Down){Fore.WHITE}\n", 0.01)

            time.sleep(AntiAFKTime)
            driver.refresh()
            type(f"\n{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Refreshed Zefoy To Prevent Session From Expiring. {Fore.LIGHTCYAN_EX}(5/5 Cool Down){Fore.WHITE}\n", 0.01)

            follows_cooldown = 0
            hearts_cooldown = 0
            views_cooldown = 0
            shares_cooldown = 0

            Follow_Seconds = 0
            Follow_Minutes = 0

            Heart_Seconds = 0
            Heart_Minutes = 0

            View_Minutes = 0
            View_Seconds = 0

            Share_Minutes = 0
            Share_Seconds = 0
            type(f"\n{Fore.LIGHTGREEN_EX}Restarting Now...\n", 0.01)
            time.sleep(34)

colorama.init()
time.sleep(7)
os.system('cls')

printBigText()
type(f'{" "*round(os.get_terminal_size().columns/2-14)}{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Made By: {Fore.LIGHTMAGENTA_EX}Dreamer#5114 {Fore.WHITE}[{Fore.LIGHTGREEN_EX}<{Fore.WHITE}]\n{" "*round(os.get_terminal_size().columns/2-30)}{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Github: {Fore.LIGHTMAGENTA_EX}https://github.com/OriginalAlien/TikTokBotter {Fore.WHITE}[{Fore.LIGHTGREEN_EX}<{Fore.WHITE}]', wait = 0.01)
printOptions()

while True:
    choice = input(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>>>{Fore.WHITE}] {Fore.GREEN}Choice: {Fore.LIGHTMAGENTA_EX}")
    if choice == "1":
        start()
        break
    elif choice == "2":
        printInfo()
    elif choice == "3":
        printOptions()
    elif choice == "4":
        clear()
    elif choice =="5":
        exit()
        
#gig
