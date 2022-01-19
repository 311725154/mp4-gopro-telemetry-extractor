
# -------   Imports -----------
import debuger
from selenium import webdriver
import selenium.webdriver.common.action_chains as act
import selenium.common.exceptions

from selenium.webdriver.common.by import By
from tkinter import messagebox as msg
import os
import time


def grab_files_from_source_dir(path):
    """
    Description: searching for mp4 files in given directory
    :return: void
    """
    files_list = []
    for obj in os.listdir(path):
        if os.path.isfile(path + '\\' + obj) and ('.MP4' in obj or '.mp4' in obj):
            files_list.append(path + '\\' + obj)

    return files_list


def extractor(source_path):
    """
    Description: extracting the telemetry data from given as a parameter mp4 files folder
    :param source_path: source of mp4 files
    :return: void
    """
    # insert the driver in to local variable path
    os.environ['PATH'] += r"C:/chromDriver/ver97"

    # activating debugger
    debug_logs = debuger.Debuger()

    # mp4 files list creation
    file_list = grab_files_from_source_dir(source_path)

    # start looping from here
    if not file_list:
        msg.showerror("Source error", "Source folder is empty!")
        exit(-1)
    else:
        for file_path in file_list:
            # web-driver object create
            driver = webdriver.Chrome()
            debug_logs.print_to_console("Grab session started:\n--------------------------\nFor file: {} \n ->\n".format(file_path))

            # start website session
            driver.get('https://goprotelemetryextractor.com/free')
            debug_logs.print_to_console("Entered to web site.")
            driver.implicitly_wait(2)

            # press the free button
            element = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-outline-primary.btn-sm.hideVersionPicker')
            driver.implicitly_wait(5)
            action = act.ActionChains(driver)
            action.move_to_element(element)
            debug_logs.print_to_console("Entered the free version.")
            driver.implicitly_wait(5)
            action.click(element)
            action.perform()
            driver.implicitly_wait(5)

            # checks if initial option engaged
            if driver.find_element(By.CSS_SELECTOR, 'p.text-white.mx-0.my-3'):
                debug_logs.print_to_console("Initial form detected...")

                # searching for email filed
                input_form = driver.find_element(By.ID, 'email')
                driver.implicitly_wait(5)
                input_form.send_keys('megoprotool@gamil.com')
                debug_logs.print_to_console("Email form field found and injected...")

                # searching for lunch button
                get_access_btn = driver.find_element(By.CSS_SELECTOR, 'input.btn.btn-light.mt-3.mb-4')
                debug_logs.print_to_console("Get access button pressed.\nWaiting for 3 seconds...")
                time.sleep(3)
                driver.implicitly_wait(3)
                action_term = act.ActionChains(driver)
                action_term.move_to_element(get_access_btn)
                action_term.click(get_access_btn)
                debug_logs.print_to_console("Performing button click")
                action_term.perform()
                driver.implicitly_wait(5)

            debug_logs.print_to_console("Performing upload of file: {}".format(file_path))
            upload_file = driver.find_element(By.XPATH, '//input[@id="gpfile"]')
            time.sleep(3)
            upload_file.send_keys(file_path)
            driver.implicitly_wait(60)
            time.sleep(45)

            # configuring the data file parameters
            debug_logs.print_to_console("Performing data file configuration")
            driver.find_element(By.XPATH, '//button[@class="btn btn-outline-primary btn-sm btn-block mt-0 mb-1 gpmf-stream"]').click()
            driver.implicitly_wait(3)

            debug_logs.print_to_console("Frames rate config")
            driver.find_element(By.XPATH, '//option[@value="frames"]').click()
            driver.implicitly_wait(3)

            debug_logs.print_to_console("Time option config")
            driver.find_element(By.XPATH, '//option[@value="MP4"]').click()
            driver.implicitly_wait(3)

            debug_logs.print_to_console("Adjusting GPS Accuracy")
            slidebar1 = driver.find_element(By.XPATH, '//input[@id="sliderForGPS5Precision"]')

            exception_flag = True
            slider = -50
            while exception_flag:
                try:
                    act.ActionChains(driver).drag_and_drop_by_offset(slidebar1, slider, 0).perform()
                    exception_flag = False
                except selenium.common.exceptions.MoveTargetOutOfBoundsException:
                    exception_flag = True
                    slider += 1
                    print("slider="+str(slider))

            debug_logs.print_to_console("Adjusting Speed Accuracy")
            slidebar2 = driver.find_element(By.XPATH, '//input[@id="sliderForGPS5Precision"]')
            act.ActionChains(driver).drag_and_drop_by_offset(slidebar2, -100, 0).perform()
            driver.implicitly_wait(3)

            debug_logs.print_to_console("Executing transformation")
            driver.find_element(By.XPATH, '//button[@gpmf-key="csv"]').click()
            driver.implicitly_wait(3)
            time.sleep(5)

            debug_logs.print_to_console("\n" * 3 + "===== file transformation finished successfully! ======")

            # close session
            driver.close()






