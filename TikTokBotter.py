#Download Chrome WebDriver
#Download Python and the modules used
#kunai#5936 and gig:) (also i recommend to execute this when you have no cool downs so it functions more properly)
import time
from colorama import Fore
import colorama
from selenium import webdriver
colorama.init()

def main(url):
    option = webdriver.ChromeOptions()
    option.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome("WEB CHROME DRIVER EXE FILE PATH HERE (use double slashes since python doesnt support single slashes, example: c:\\user\\users\\webdrive.exe)", options=option)
    driver.set_window_size(777, 777)
    driver.get('https://zefoy.com')
    amount = 0

    captcha_finish = input(f"{Fore.YELLOW}\nPlease Solve The Captcha On The Website To Continue.\nType \"y\" Once You Finished The Captcha.\n\n> {Fore.WHITE}")

    if captcha_finish == "y":

        print("Starting Now!\n")

        follows_cooldown = 0
        hearts_cooldown = 0
        views_cooldown = 0
        shares_cooldown = 0

        while captcha_finish == "y":
            try:
                #Follows, id=1
                driver.find_element_by_xpath('/html/body/nav/ul/li/a').click() #Goes To Zefoy Home
                print(f"{Fore.YELLOW}Waiting For Follows Cool Down.{Fore.WHITE}")
                time.sleep(follows_cooldown) #waiting cooldown
                follows_cooldown = 0 #resets cooldown
                driver.find_element_by_xpath('/html/body/nav/ul/li/a').click()
                driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/div/button').click() #goes to the follow page
                driver.find_element_by_xpath('//*[@id="sid"]/div/form/div/input').send_keys(url) #types the url
                driver.find_element_by_xpath('//*[@id="sid"]/div/form/div/div/button').click() #searches
                time.sleep(3) #waits
                driver.find_element_by_xpath('//*[@id="c2VuZF9mb2xsb3dlcnNfdGlrdG9r"]/div[1]/div/form/button').click() #sends
                print(f"{Fore.LIGHTGREEN_EX}\nSent Followers!\n{Fore.WHITE}")
                print(f"{Fore.YELLOW}Getting Cool Down...{Fore.WHITE}")
                time.sleep(5)
                follows_cooldownUnformat = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/h4').text #getting cooldown

                if follows_cooldownUnformat[13] == " ": #some string slicing and int converting
                    follows_cooldownFormat = int(follows_cooldownUnformat[12])*60
                elif follows_cooldownUnformat[13] != " ":
                    follows_cooldownFormat = int(follows_cooldownUnformat[12:14])*60

                follows_cooldown += follows_cooldownFormat #sets the cooldown
                follows_cooldown += 60 #plus 60 seconds jus to make sure yk
                print(f"{Fore.GREEN}Follows Cool Down Minutes: {follows_cooldown/60}{Fore.WHITE}")

                driver.find_element_by_xpath('/html/body/nav/ul/li/a').click() #goes back to home for next sending
            except: #if a error occurs then do this
                print(f"{Fore.RED}Unknown Error Occurred When Trying to Send Follows{Fore.WHITE}") 

            try:
                #Hearts, id=2
                driver.find_element_by_xpath('/html/body/nav/ul/li/a').click() #goes home
                print(f"{Fore.YELLOW}Waiting For Hearts Cool Down.{Fore.WHITE}")
                time.sleep(hearts_cooldown) #waits cooldown
                hearts_cooldown = 0 #resets
                driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/button').click() #goes to heart page
                driver.find_element_by_xpath('//*[@id="sid2"]/div/form/div/input').send_keys(url) #sends the url
                driver.find_element_by_xpath('//*[@id="sid2"]/div/form/div/div/button').click() #searches
                time.sleep(3)
                driver.find_element_by_xpath('//*[@id="c2VuZE9nb2xsb3dlcnNfdGlrdG9r"]/div[1]/div/form/button').click() #sends
                print(f"{Fore.LIGHTGREEN_EX}\nSent Hearts!\n{Fore.WHITE}")
                print(f"{Fore.YELLOW}Getting Cool Down...{Fore.WHITE}")
                time.sleep(5)
                hearts_cooldownUnformat = driver.find_element_by_xpath("/html/body/div[4]/div[3]/div/div/h4").text #gets the cooldown

                if hearts_cooldownUnformat[13] == " ": #we do a little string slice and mafth :)
                    hearts_cooldownFormat = int(hearts_cooldownUnformat[12])*60
                elif hearts_cooldownUnformat[13] != " ":
                    hearts_cooldownFormat = int(hearts_cooldownUnformat[12:14])*60

                hearts_cooldown += hearts_cooldownFormat #sets cooldown
                hearts_cooldown += 60 #add extra so yk
                print(f"{Fore.GREEN}Hearts Cool Down Mintues: {hearts_cooldown/60}{Fore.WHITE}")

                driver.find_element_by_xpath('/html/body/nav/ul/li/a').click() #goes back home
                
            except: #if error happen then do this
                print(f"{Fore.RED}Unknown Error Occurred When Attempting To Send Hearts{Fore.WHITE}")

            try:
                #Views, id=4
                driver.find_element_by_xpath('/html/body/nav/ul/li/a').click() #goes to home
                print(f"{Fore.YELLOW}Waiting For Views Cool Down.{Fore.WHITE}")
                time.sleep(views_cooldown) #waits for cooldown
                views_cooldown = 0 #resets cooldown
                driver.find_element_by_xpath('//*[@id="main"]/div/div[4]/div/button').click() #goes to views page
                driver.find_element_by_xpath('//*[@id="sid4"]/div/form/div/input').send_keys(url) #type url
                driver.find_element_by_xpath('//*[@id="sid4"]/div/form/div/div/button').click() #searches
                time.sleep(3)
                driver.find_element_by_xpath('//*[@id="c2VuZC9mb2xsb3dlcnNfdGlrdG9V"]/div[1]/div/form/button').click() #sends
                print(f"{Fore.LIGHTGREEN_EX}\nSent Views!\n{Fore.WHITE}")
                print(f"{Fore.YELLOW}Getting Cool Down...{Fore.WHITE}")
                time.sleep(5)
                views_cooldownUnformat = driver.find_element_by_xpath("/html/body/div[4]/div[5]/div/div/h4").text #gets cooldown

                if views_cooldownUnformat[13] == " ": #string slice + math
                    views_cooldownFormat = int(views_cooldownUnformat[12])*60
                elif views_cooldownUnformat[13] != " ":
                    views_cooldownFormat = int(views_cooldownUnformat[12:14])*60

                views_cooldown += views_cooldownFormat #sets cooldown
                views_cooldown += 60 #add extra yk
                print(f"{Fore.GREEN}Views Cool Down Minute: {views_cooldown/60} {Fore.WHITE}")

                driver.find_element_by_xpath('/html/body/nav/ul/li/a').click()
            except:
                print(f"{Fore.RED}Unknown Error Occurred When Attempting To Send Views{Fore.WHITE}")

            try:
                #Shares, id=7
                driver.find_element_by_xpath('/html/body/nav/ul/li/a').click() #tired of writing comments but this jus goes to home page
                print(f"{Fore.YELLOW}Waiting For Shares Cool Down.{Fore.WHITE}")
                time.sleep(shares_cooldown) #waits cooldown
                shares_cooldown = 0
                driver.find_element_by_xpath('//*[@id="main"]/div/div[5]/div/button').click() #goes to share 
                driver.find_element_by_xpath('//*[@id="sid7"]/div/form/div/input').send_keys(url) #types url
                driver.find_element_by_xpath('//*[@id="sid7"]/div/form/div/div/button').click() #searches
                time.sleep(3)
                driver.find_element_by_xpath('//*[@id="c2VuZC9mb2xsb3dlcnNfdGlrdG9s"]/div[1]/div/form/button').click() #sends
                print(f"{Fore.LIGHTGREEN_EX}\nSent Shares!\n{Fore.WHITE}")
                print(f"{Fore.YELLOW}Getting Cool Down...{Fore.WHITE}")
                time.sleep(5)
                shares_cooldownUnformat = driver.find_element_by_xpath('/html/body/div[4]/div[6]/div/div/h4').text #gets cooldown

                if shares_cooldownUnformat[13] == " ": #string slice and math
                    shares_cooldownFormat = int(shares_cooldownUnformat[12])*60
                elif shares_cooldownUnformat[13] != " ":
                    shares_cooldownFormat = int(shares_cooldownUnformat[12:14])*60
                
                shares_cooldown += shares_cooldownFormat #sets cooldown
                shares_cooldown += 60 #add extra
                print(f"{Fore.GREEN}Shares Cool Down Minutes: {shares_cooldown/60} {Fore.WHITE}\n")

                driver.find_element_by_xpath('/html/body/nav/ul/li/a').click() #goes home

                amount += 1 #since this is the last sending then it adds 1 to amount
                print(f"{Fore.GREEN}\nSent Followers, Hearts, Views, & Shares {amount} Times.{Fore.WHITE}")
                print(f"\n{Fore.LIGHTGREEN_EX}Current Cool Downs In Minutes\n\nFollow: {follows_cooldown/60}\nHearts: {hearts_cooldown/60}\nViews: {views_cooldown/60}\nShares: {shares_cooldown/60}\nHere's Some Water While Waiting For The Cool Down :) 🌊 🧊 🥤{Fore.WHITE}\n")
                
                LargestCoolDown = [follows_cooldown, hearts_cooldown, views_cooldown, shares_cooldown]
                LargestCoolDown.sort()
                time.sleep(LargestCoolDown[-1])
                follows_cooldown = 0
                hearts_cooldown = 0
                views_cooldown = 0
                shares_cooldown = 0

            except: #if error do this
                print(f"{Fore.RED}Unknown Error Occurred When Attempting To Send Shares{Fore.WHITE}")


print(f"""
{Fore.LIGHTGREEN_EX}████████╗██╗██╗  ██╗{Fore.GREEN}████████╗ ██████╗ ██╗  ██╗    {Fore.BLUE}██████╗  ██████╗ ████████╗████████╗███████╗██████╗     
{Fore.LIGHTGREEN_EX}╚══██╔══╝██║██║ ██╔╝{Fore.GREEN}╚══██╔══╝██╔═══██╗██║ ██╔╝    {Fore.BLUE}██╔══██╗██╔═══██╗╚══██╔══╝╚══██╔══╝██╔════╝██╔══██╗    
{Fore.LIGHTGREEN_EX}   ██║   ██║█████╔╝ {Fore.GREEN}   ██║   ██║   ██║█████╔╝     {Fore.BLUE}██████╔╝██║   ██║   ██║      ██║   █████╗  ██████╔     
{Fore.GREEN}   ██║   ██║██╔═██╗  {Fore.LIGHTGREEN_EX}  ██║   ██║   ██║██╔═██╗     {Fore.LIGHTCYAN_EX}██╔══██╗██║   ██║   ██║      ██║   ██╔══╝  ██╔══██╗   
{Fore.GREEN}   ██║   ██║██║  ██╗ {Fore.LIGHTGREEN_EX}  ██║   ╚██████╔╝██║  ██╗    {Fore.LIGHTCYAN_EX}██████╔╝╚██████╔╝   ██║      ██║   ███████╗██║  ██║ 
{Fore.GREEN}   ╚═╝   ╚═╝╚═╝  ╚═╝{Fore.LIGHTGREEN_EX}   ╚═╝    ╚═════╝ ╚═╝  ╚═╝    {Fore.LIGHTBLUE_EX}╚═════╝  ╚═════╝    ╚═╝      ╚═╝   ╚══════╝╚═╝  ╚═╝ 
""")

print(f"{Fore.YELLOW}________________{Fore.RED}!! NOTICE !!{Fore.YELLOW}_________________\n\n1. The Cool Down Finder In This Code Only\n   Supports 1-2 Digits.\n\n2. Educational Purpose Only, Not Responsible\n   If Anything Bad Happens To You.\n\n3. Contact kunai#5936 If You Need Assistance\n\n4. There Will Be Lots Of Logs Because Of The\n   Web Driver Logs So Most Text Besides Logs Will Be\n   Hilighted As A Color.\n\n5. Please Do Not Interact With Tabs With The Chrome\n   Web Driver When It's Running Since It Can Cause Errors.\n\n6. The Cool Down May Take Longer As Expected Because Me No Know How To Make An Actual Timer Inside A Loop.\n\n7. Enjoy And Yeah!\n______________________________________________{Fore.WHITE}")
print(f"{Fore.LIGHTGREEN_EX}\nMade By: kunai#5936 :)")
print(f"{Fore.LIGHTGREEN_EX}Also Credits TO https://github.com/darkp3ter/ Since He Inspired Me To Make This.{Fore.WHITE}")
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
