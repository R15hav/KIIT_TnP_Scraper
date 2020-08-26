# KIIT_TnP_Scraper v1.0

## Setup
1. **Scrape_tnp** is the main python file.
2. Before running the code put your *id* and *password* in the mentioned area in the **kiit_code.py** file.
3. Now go to **twilio** and get an account and activate sandbox ([follow this Link](https://www.twilio.com/blog/send-whatsapp-message-30-seconds-python))
4. Put the sand box phone number in the **tnp_whatsapp.py** file at the mentioned line.

## Where to run the code?
1. In order to run the code you need to host the code on some code hosting platforms like *[Pythonanywhere](https://www.pythonanywhere.com)*
2. Since this code runs a selenium web driver to scrape the site we need to run a virtual display while hosting the code on *[Pythonanywhere](https://www.pythonanywhere.com)*    using the command `xvfb-run -a python3.6 /home/myusername/myfolder/myscript.py` *([more on](https://help.pythonanywhere.com/pages/selenium/))*
3. To run the code at intervals *[link](https://help.pythonanywhere.com/pages/ScheduledTasks/)*

## future updates
I am working on how to get the pdf file sent to ones *whatsapp*.
