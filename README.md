# KIIT_TnP_Scraper v1.0

## Requirements
1. Python 3.6
2. ### Modules - **If and only if you are running this code on a local machine**
  - [Selenium](https://pypi.org/project/selenium/)
  - [Selenium mozila web drivers- Geko driver](https://github.com/mozilla/geckodriver/releases)
  - [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)

## Setup
1. **Scrape_tnp** is the main python file.
2. Before running the code put your *id* and *password* in the mentioned area in the **kiit_code.py** file.
3. Get the geko driver on your pc and Enter your Driver location at the specified position on the **kiit_code.py** file.
3. Now go to **twilio** and get an account and activate sandbox ([follow this Link](https://www.twilio.com/blog/send-whatsapp-message-30-seconds-python))
4. Put the sand box phone number in the **tnp_whatsapp.py** file at the mentioned line.

## Where to run the code?
- ### On windows:-
1. Download the zipped code files extract it on your local machine.
2. pip install all the required modules from above.
3. Follow the setup procedure and you are good to go.
4. Open terminal and run `python Scrape_tnp.py`. 
5. Leave the rest to the bot.
- ### Better Way:-
1. In order to run the code you need to host the code on some cloud platforms like *[Pythonanywhere](https://www.pythonanywhere.com)*
3. Create an account, upload all the files.
2. Since this code runs a selenium web driver to scrape the site we need to run a virtual display while hosting the code on *[Pythonanywhere](https://www.pythonanywhere.com)*    using the command `xvfb-run -a python3.6 /home/myusername/myfolder/myscript.py` *([more on](https://help.pythonanywhere.com/pages/selenium/))*
3. To run the code at intervals *[link](https://help.pythonanywhere.com/pages/ScheduledTasks/)*

## future updates
I am working on how to get the pdf file sent to ones *whatsapp*.

**[Kiit TnP](https://kiittnp.in/ea19b38134d463acc8c7b66744a481847ab4b/)**
