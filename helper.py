import time

def scroll_to_bottom(driver):
    SCROLL_PAUSE_TIME = 0.5
    JS_DICTIONARY = {'get_scroll_height': 'return document.body.scrollHeight;', 'scroll_to': 'window.scrollTo(0, document.body.scrollHeight);'}

    # Get scroll height
    initial_height = driver.execute_script(JS_DICTIONARY['get_scroll_height'])

    while True:
        driver.execute_script(JS_DICTIONARY['scroll_to'])
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script(JS_DICTIONARY['get_scroll_height'])

        if new_height == initial_height:
            break
        initial_height = new_height