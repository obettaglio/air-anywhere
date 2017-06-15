from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

dr = webdriver.PhantomJS()

dr.get('https://www.skyscanner.com/')

dr.find_element_by_id('#js-one-way-input').click()

origin = dr.find_element_by_id('#js-origin-input')
origin.clear()
origin.send_keys('')  # import origin

destination = dr.find_element_by_id('#js-destination-input')
destination.clear()
destination.send_keys('')     # import destination

dr.find_element_by_id('#js-search-button').click()

try:
    element = WebDriverWait(dr, 10).until(
        EC.invisibility_of_element_located(By.CLASS_NAME, 'month-spinner')
    )
finally:
    dr.quit()


## NEXT STEPS:

# explicit wait
# for each td.calendar-day table-selected
# click first td > div > span.table-price small
# click .backpack-button
# explicit wait
# in ul.day-list
# find first li.day-list-item
#   > div.card-body > section.card-main
#       > span.text ---> airline
#       > div.leg-details > div.depart > span.station-tooltip > span.times ---> departure time
#                                                             > span.stop-station ---> origin airport
#       > div.leg-details > div.stops > span.station-tooltip > span.duration ---> duration
#       > div.leg-details > div.arrive > span.station-tooltip > span.times ---> arrival time
#                                                             > span.stop-station ---> destination airport
