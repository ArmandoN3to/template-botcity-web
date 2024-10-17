"""
WARNING:

Please make sure you install the bot dependencies with `pip install --upgrade -r requirements.txt`

"""


# Import for the Web Bot
from botcity.web import WebBot, Browser, By

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *
from webdriver_manager.chrome import ChromeDriverManager


# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False


class Bot(WebBot):
    

    def action(self,execution = None):
        # Runner passes the server url, the id of the task being executed,
        # the access token and the parameters that this task receives (when applicable).
        maestro = BotMaestroSDK.from_sys_args()
        ## Fetch the BotExecution with details from the task, including parameters
        execution = maestro.get_execution()

        print(f"Task ID is: {execution.task_id}")
        print(f"Task Parameters are: {execution.parameters}")

        

        # Configure whether or not to run on headless mode
        self.headless = False

        self.browser = Browser.CHROME
        self.driver_path = ChromeDriverManager().install()

        self.browse("https://www.botcity.dev")

        # Implement here your logic...
        try:
            pass

        except Exception as e:
            print(e)
            self.save_screenshot('erro.png')

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
