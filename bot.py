"""
WARNING:

Please make sure you install the bot dependencies with `pip install --upgrade -r requirements.txt`

"""


from botcity.web import WebBot, Browser, By

from botcity.maestro import *
from webdriver_manager.chrome import ChromeDriverManager


# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False


class Bot(WebBot):
    
    def bot_configuration(self)->None:
        # Configure whether or not to run on headless mode
        self.headless = False
        self.browser = Browser.CHROME
        self.driver_path = ChromeDriverManager().install()

    def start_browser_bot(self,url= "https://www.botcity.dev"):
        try:
            self.browse(url)
        except Exception as ex:

            print('Error starting browser')
            self.save_screenshot('error.png')


    def action(self,execution = None):
        # Runner passes the server url, the id of the task being executed,
        # the access token and the parameters that this task receives (when applicable).
        maestro = BotMaestroSDK.from_sys_args()
        ## Fetch the BotExecution with details from the task, including parameters
        execution = maestro.get_execution()

        print(f"Task ID is: {execution.task_id}")
        print(f"Task Parameters are: {execution.parameters}")

        # Implement here your logic...
        try:
            self.bot_configuration()
            self.start_browser_bot()         #inserir Url ou por padrao vai para o site da BOTCITY

        except Exception as ex:
            print(ex)
            self.save_screenshot('error.png')

        finally:
            # Wait 3 seconds before closing
            self.wait(3000)
            self.stop_browser()

            # Uncomment to mark this task as finished on BotMaestro
            # maestro.finish_task(
            #     task_id=execution.task_id,
            #     status=AutomationTaskFinishStatus.SUCCESS,
            #     message="Task Finished OK."
            # )


    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()
