import time
from colorama import Fore
from colorama import init
from selenium import webdriver
init()

def main(url):
    option = webdriver.ChromeOptions()
    option.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome("Chrome Web Driver File Path, Use Double Back Slash, Example: C:\\Users\USER\\Desktop\\chromedriver\\chromedriver.exe", options=option)
    driver.set_window_size(777, 777)
    driver.get('https://zefoy.com')
    amount = 0

    captcha_finish = input(f"{Fore.YELLOW}\nPlease Solve The Captcha To Continue.\nType \"y\" Once You Finished The Captcha.\n\n> {Fore.WHITE}")

    if captcha_finish == "y":

        print("Starting Now!\n")

        follows_cooldown = 0
        hearts_cooldown = 0
        views_cooldown = 0
        shares_cooldown = 0

        Follow_Continue1 = False
        Follow_Continue2 = False
        Heart_Continue1 = False
        Heart_Continue2 = False
        View_Continue1 = False
        View_Continue2 = False
        Share_Continue1 = False
        Share_Continue2 = False

        while captcha_finish == "y":
            try:
                driver.find_element_by_xpath('/html/body/nav/ul/li/a').click() #Goes To Zefoy Home
                follows_cooldown = 0 #resets cooldown

                try:
                    driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/div/button').click() #goes to the follow page
                    driver.find_element_by_xpath('//*[@id="sid"]/div/form/div/input').send_keys(url) #types the url
                    Follow_Continue1 = True
                except:
                    print(f"{Fore.RED}Follower Send Page Is Down.\nSkipping...{Fore.WHITE}")
                    Follow_Continue1 = False
                    Follow_Seconds = 0
                    Follow_Minutes = 0

                if Follow_Continue1 == True:
                    driver.find_element_by_xpath('//*[@id="sid"]/div/form/div/div/button').click() #searches
                    time.sleep(5) #waits
                    try:
                        driver.find_element_by_xpath('//*[@id="c2VuZF9mb2xsb3dlcnNfdGlrdG9r"]/div[1]/div/form/button').click() #sends
                        Follow_Continue2 = True
                    except:
                        print(f"{Fore.RED}Follow Cool Down Isn't Finished Yet. Getting Cool Down And Skipping...\n {Fore.WHITE}")
                        Follow_Continue2 = False
                        Follow_Text = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div/h4").text

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

                        print(f"{Fore.LIGHTGREEN_EX}Follow Cool Down Is {Fore.CYAN}{Follow_Minutes}{Fore.LIGHTGREEN_EX} Minutes And {Fore.CYAN}{Follow_Seconds%60}{Fore.LIGHTGREEN_EX} Seconds.{Fore.WHITE}")

                    if Follow_Continue2 == True:
                        print(f"{Fore.LIGHTGREEN_EX}\nSent Followers!\n{Fore.WHITE}")
                        print(f"{Fore.YELLOW}Getting Cool Down...{Fore.WHITE}")
                        time.sleep(5)
                        Follow_Text = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/h4').text #getting cooldown

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

                        print(f"{Fore.LIGHTGREEN_EX}Follow Cool Down Is {Fore.CYAN}{Follow_Minutes}{Fore.LIGHTGREEN_EX} Minutes And {Fore.CYAN}{Follow_Seconds%60}{Fore.LIGHTGREEN_EX} Seconds.{Fore.WHITE}")

                        driver.find_element_by_xpath('/html/body/nav/ul/li/a').click() #goes back to home for next sending

                    else:
                        pass
                else:
                    pass

            except: #if a error occurs then do this
                print(f"{Fore.RED}Unknown Error Occurred When Trying to Send Follows{Fore.WHITE}") 



            try:
                #Hearts, id=2
                driver.find_element_by_xpath('/html/body/nav/ul/li/a').click() #goes home
                hearts_cooldown = 0 #resets

                try:
                    driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/button').click() #goes to heart page
                    driver.find_element_by_xpath('//*[@id="sid2"]/div/form/div/input').send_keys(url) #sends the url
                    Heart_Continue1 = True
                except:
                    print(f"{Fore.RED}Heart Send Page Is Down.\nSkipping...{Fore.WHITE}")
                    Heart_Continue1 = False
                    Heart_Seconds = 0
                    Heart_Minutes = 0

                if Heart_Continue1 == True:
                    driver.find_element_by_xpath('//*[@id="sid2"]/div/form/div/div/button').click() #searches
                    time.sleep(5)
                    try:
                        driver.find_element_by_xpath('//*[@id="c2VuZE9nb2xsb3dlcnNfdGlrdG9r"]/div[1]/div/form/button').click() #sends
                        Heart_Continue2 = True

                    except:
                        print(f"{Fore.RED}Heart Cool Down Isn't Finished Yet. Getting Cool Down And Skipping...\n {Fore.WHITE}")
                        Heart_Continue2 = False
                        Heart_Text = driver.find_element_by_xpath("/html/body/div[4]/div[3]/div/div/h4").text

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

                        Heart_Seconds += 57
                        hearts_cooldown += Heart_Seconds

                        print(f"{Fore.LIGHTGREEN_EX}Heart Cool Down Is {Fore.CYAN}{Heart_Minutes}{Fore.LIGHTGREEN_EX} Minutes And {Fore.CYAN}{Heart_Seconds%60}{Fore.LIGHTGREEN_EX} Seconds.{Fore.WHITE}")

                    if Heart_Continue2 == True:
                        print(f"{Fore.LIGHTGREEN_EX}\nSent Hearts!\n{Fore.WHITE}")
                        print(f"{Fore.YELLOW}Getting Cool Down...{Fore.WHITE}")
                        time.sleep(5)

                        Heart_Text = driver.find_element_by_xpath("/html/body/div[4]/div[3]/div/div/h4").text

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

                        print(f"{Fore.LIGHTGREEN_EX}Heart Cool Down Is {Fore.CYAN}{Heart_Minutes}{Fore.LIGHTGREEN_EX} Minutes And {Fore.CYAN}{Heart_Seconds%60}{Fore.LIGHTGREEN_EX} Seconds.{Fore.WHITE}")

                        driver.find_element_by_xpath('/html/body/nav/ul/li/a').click() #goes back home
                    else:
                        pass
                else:
                    pass
                
            except: #if error happen then do this
                print(f"{Fore.RED}Unknown Error Occurred When Attempting To Send Hearts{Fore.WHITE}")

            try:
                #Views, id=4
                driver.find_element_by_xpath('/html/body/nav/ul/li/a').click() #goes to home
                try:
                    driver.find_element_by_xpath('//*[@id="main"]/div/div[4]/div/button').click() #goes to views page
                    driver.find_element_by_xpath('//*[@id="sid4"]/div/form/div/input').send_keys(url) #type url
                    View_Continue1 = True
                except:
                    print(f"{Fore.RED}Views Send Page Is Down.\nSkipping...{Fore.WHITE}")
                    View_Continue1 = False
                    View_Seconds = 0
                    View_Minutes = 0

                if View_Continue1 == True:
                    driver.find_element_by_xpath('//*[@id="sid4"]/div/form/div/div/button').click() #searches
                    time.sleep(5)
                    try:
                        driver.find_element_by_xpath('/html/body/div[4]/div[5]/div/div/div[1]/div/form/button').click() #sends
                        View_Continue2 = True
                    except:

                        View_Continue2 = False
                        View_Text = driver.find_element_by_xpath("/html/body/div[4]/div[5]/div/div/h4").text #gets the cooldown
                        print(f"{Fore.RED}View Cool Down Isn't Finished Yet. Getting Cool Down And Skipping...\n {Fore.WHITE}")

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

                        print(f"{Fore.LIGHTGREEN_EX}View Cool Down Is {Fore.CYAN}{View_Minutes}{Fore.LIGHTGREEN_EX} Minutes And {Fore.CYAN}{View_Seconds%60}{Fore.LIGHTGREEN_EX} Seconds.{Fore.WHITE}")

                    if View_Continue2 == True:
                        print(f"{Fore.LIGHTGREEN_EX}\nSent Views!\n{Fore.WHITE}")
                        print(f"{Fore.YELLOW}Getting Cool Down...{Fore.WHITE}")
                        time.sleep(5)

                        View_Text = driver.find_element_by_xpath("/html/body/div[4]/div[5]/div/div/h4").text #gets the cooldown

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

                        print(f"{Fore.LIGHTGREEN_EX}View Cool Down Is {Fore.CYAN}{View_Minutes}{Fore.LIGHTGREEN_EX} Minutes And {Fore.CYAN}{View_Seconds%60}{Fore.LIGHTGREEN_EX} Seconds.{Fore.WHITE}")

                        driver.find_element_by_xpath('/html/body/nav/ul/li/a').click()

                    else:
                        pass

                else:
                    pass
                    
            except:
                print(f"{Fore.RED}Unknown Error Occurred When Attempting To Send Views{Fore.WHITE}")

            try:
                #Shares, id=7
                driver.find_element_by_xpath('/html/body/nav/ul/li/a').click() #tired of writing comments but this jus goes to home page

                try:
                    driver.find_element_by_xpath('//*[@id="main"]/div/div[5]/div/button').click() #goes to share 
                    driver.find_element_by_xpath('//*[@id="sid7"]/div/form/div/input').send_keys(url) #types url
                    Share_Continue1 = True
                except:
                    Share_Continue1 = False
                    print(f"{Fore.RED}Share Send Page Is Down.\nSkipping...{Fore.WHITE}")
                    Share_Minutes = 0
                    Share_Seconds = 0

                if Share_Continue1 == True:
                    driver.find_element_by_xpath('//*[@id="sid7"]/div/form/div/div/button').click() #searches
                    time.sleep(5)
                    try:
                        driver.find_element_by_xpath('//*[@id="c2VuZC9mb2xsb3dlcnNfdGlrdG9s"]/div[1]/div/form/button').click() #sends
                        Share_Continue2 = True
                    except:
                        Share_Continue2 = False
                        print(f"{Fore.RED}Share Cool Down Isn't Finished Yet. Getting Cool Down And Skipping...\n {Fore.WHITE}")
                        Share_Text = driver.find_element_by_xpath('/html/body/div[4]/div[6]/div/div/h4').text #gets cooldown

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

                        print(f"{Fore.LIGHTGREEN_EX}Share Cool Down Is {Fore.CYAN}{Share_Minutes}{Fore.LIGHTGREEN_EX} Minutes And {Fore.CYAN}{Share_Seconds%60}{Fore.LIGHTGREEN_EX} Seconds.{Fore.WHITE}")

                    if Share_Continue2 == True:
                        print(f"{Fore.LIGHTGREEN_EX}\nSent Shares!\n{Fore.WHITE}")
                        print(f"{Fore.YELLOW}Getting Cool Down...{Fore.WHITE}")
                        time.sleep(5)
                        Share_Text = driver.find_element_by_xpath('/html/body/div[4]/div[6]/div/div/h4').text #gets cooldown

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

                        print(f"{Fore.LIGHTGREEN_EX}Share Cool Down Is {Fore.CYAN}{Share_Minutes}{Fore.LIGHTGREEN_EX} Minutes And {Fore.CYAN}{Share_Seconds%60}{Fore.LIGHTGREEN_EX} Seconds.{Fore.WHITE}")

                        driver.find_element_by_xpath('/html/body/nav/ul/li/a').click() #goes home

            except:
                print(f"{Fore.RED}Unknown Error Occurred When Attempting To Send Shares{Fore.WHITE}")
            #
            driver.find_element_by_xpath('/html/body/nav/ul/li/a').click() #goes home
            amount += 1
            print(f"{Fore.GREEN}\nSent Followers, Hearts, Views, & Shares {amount} Times.{Fore.WHITE}")
            print(f"\n{Fore.LIGHTGREEN_EX}Current Cool Downs\n\nFollow: {Follow_Seconds} Minutes and {follows_cooldown%60} Seconds. ({follows_cooldown} Seconds)\nHearts: {Heart_Minutes} Minutes and {hearts_cooldown%60} Seconds. ({hearts_cooldown} Seconds)\nViews: {View_Minutes} Minutes and {views_cooldown%60} Seconds. ({views_cooldown} Seconds)\nShares: {Share_Minutes} Minutes And {shares_cooldown%60} Seconds. ({shares_cooldown} Seconds)\nHere's Some Water While Waiting For The Cool Down :) 🌊 🧊 🥤{Fore.WHITE}\n")

            LargestCoolDown = [follows_cooldown, hearts_cooldown, views_cooldown, shares_cooldown]
            LargestCoolDown.sort()
            AntiAFKTime = int(LargestCoolDown[-1])/5

            time.sleep(AntiAFKTime)
            driver.find_element_by_xpath('/html/body/nav/ul/li/a').click()
            print(f"\n{Fore.LIGHTGREEN_EX}Refreshed Zefoy To Prevent Session From Expiring.{Fore.WHITE}")
            print(f"{Fore.RED}!! Reminder !!\nPlease Do Not Interact With The Tabs In Chrome Web Driver As It Can Mess Up The Code And Give Errors\n")

            time.sleep(AntiAFKTime)
            driver.find_element_by_xpath('/html/body/nav/ul/li/a').click()
            print(f"\n{Fore.LIGHTGREEN_EX}Refreshed Zefoy To Prevent Session From Expiring.{Fore.WHITE}")

            time.sleep(AntiAFKTime)
            driver.find_element_by_xpath('/html/body/nav/ul/li/a').click()
            print(f"\n{Fore.LIGHTGREEN_EX}Refreshed Zefoy To Prevent Session From Expiring.{Fore.WHITE}")

            time.sleep(AntiAFKTime)
            driver.find_element_by_xpath('/html/body/nav/ul/li/a').click()
            print(f"\n{Fore.LIGHTGREEN_EX}Refreshed Zefoy To Prevent Session From Expiring.{Fore.WHITE}")

            time.sleep(AntiAFKTime)
            driver.find_element_by_xpath('/html/body/nav/ul/li/a').click()
            print(f"\n{Fore.LIGHTGREEN_EX}Refreshed Zefoy To Prevent Session From Expiring.{Fore.WHITE}")

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


print(f"""
{Fore.LIGHTGREEN_EX}████████╗██╗██╗  ██╗{Fore.GREEN}████████╗ ██████╗ ██╗  ██╗    {Fore.BLUE}██████╗  ██████╗ ████████╗████████╗███████╗██████╗     
{Fore.LIGHTGREEN_EX}╚══██╔══╝██║██║ ██╔╝{Fore.GREEN}╚══██╔══╝██╔═══██╗██║ ██╔╝    {Fore.BLUE}██╔══██╗██╔═══██╗╚══██╔══╝╚══██╔══╝██╔════╝██╔══██╗    
{Fore.LIGHTGREEN_EX}   ██║   ██║█████╔╝ {Fore.GREEN}   ██║   ██║   ██║█████╔╝     {Fore.BLUE}██████╔╝██║   ██║   ██║      ██║   █████╗  ██████╔     
{Fore.GREEN}   ██║   ██║██╔═██╗  {Fore.LIGHTGREEN_EX}  ██║   ██║   ██║██╔═██╗     {Fore.LIGHTCYAN_EX}██╔══██╗██║   ██║   ██║      ██║   ██╔══╝  ██╔══██╗   
{Fore.GREEN}   ██║   ██║██║  ██╗ {Fore.LIGHTGREEN_EX}  ██║   ╚██████╔╝██║  ██╗    {Fore.LIGHTCYAN_EX}██████╔╝╚██████╔╝   ██║      ██║   ███████╗██║  ██║ 
{Fore.GREEN}   ╚═╝   ╚═╝╚═╝  ╚═╝{Fore.LIGHTGREEN_EX}   ╚═╝    ╚═════╝ ╚═╝  ╚═╝    {Fore.LIGHTBLUE_EX}╚═════╝  ╚═════╝    ╚═╝      ╚═╝   ╚══════╝╚═╝  ╚═╝ 
""")

print(f"{Fore.YELLOW}________________{Fore.RED}!! NOTICE !!{Fore.YELLOW}_________________\n\n1. The Cool Down Finder In This Code Only\n   Supports 1-2 Digits.\n\n2. Educational Purpose Only, Not Responsible\n   If Anything Bad Happens To You.\n\n3. Contact kunai#5936 If You Need Assistance\n\n4. There Will Be Lots Of Logs Because Of The\n   Web Driver Logs So Most Text Besides Logs Will Be\n   Hilighted As A Color.\n\n5. Please Do Not Interact With Tabs With The Chrome\n   Web Driver When It's Running Since It Can Cause Errors.\n\n6. The Cool Down May Take Longer As Expected Because\n   Me No Know How To Make An Actual Timer Inside A Loop.\n\n7. Enjoy And Yeah!\n______________________________________________{Fore.WHITE}")
print(f"{Fore.LIGHTGREEN_EX}\nUPDATES: Advanced Trouble Shooting, Better Wait Time, & Anti Session Expire")
print(f"{Fore.LIGHTGREEN_EX}\nMade By: Dreamer#5114 (Changed My Discord Tag) :)")
print(f"{Fore.LIGHTGREEN_EX}\nAlso Credits To https://github.com/darkp3ter/ Since He Inspired Me To Make This.{Fore.WHITE}")
print(f"{Fore.LIGHTGREEN_EX}Enjoy!\n")
print(f"\n{Fore.LIGHTWHITE_EX}Github: {Fore.WHITE}https://github.com/OriginalAlien")
print(f"{Fore.LIGHTRED_EX}Download {Fore.LIGHTGREEN_EX}Chrome {Fore.LIGHTYELLOW_EX}Driver: {Fore.LIGHTBLUE_EX}https://chromedriver.chromium.org/downloads")
print(f"{Fore.BLUE}Download Python: {Fore.YELLOW}https://python.org/download{Fore.WHITE}")

video_url = input("\nVideo URL: ") #video url
print(f"{Fore.LIGHTGREEN_EX}Opening Chrome Web Driver...{Fore.WHITE}")

while "tiktok" not in video_url: #if possibly invalid link then...
    print(f"{Fore.RED}Please Enter A Valid Link.{Fore.WHITE}")
    video_url = input("\nVideo URL: ")
    if "tiktok" in video_url:
        print(f"{Fore.LIGHTGREEN_EX}Opening Chrome Web Driver...{Fore.WHITE}")
        break

main(video_url) #calls function and sets parameter as the input
