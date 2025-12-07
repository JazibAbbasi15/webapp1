from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

# ---------------- SETUP ---------------- #
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # run headless
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")
options.add_argument("--no-sandbox")

driver = webdriver.Chrome( options=options)
wait = WebDriverWait(driver, 15)

# Create screenshots folder
#os.makedirs("screenshots", exist_ok=True)

# ---------------- OPEN SITE ---------------- #
driver.get("http://user-frontend-ci:5173/login")
time.sleep(1)
#driver.save_screenshot("screenshots/01_open_site.png")

# ---------------- LOGIN ---------------- #
login_here = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "p.cursor-pointer:nth-child(2)")))
driver.execute_script("arguments[0].click();", login_here)
time.sleep(1)
#driver.save_screenshot("screenshots/02_clicked_login_here.png")

email_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="email"]')))
email_field.send_keys("test123@gmail.com")
password_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="password"]')))
password_field.send_keys("12345678")

signin_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.bg-black")))
driver.execute_script("arguments[0].click();", signin_button)
print("Login completed!")
time.sleep(3)  # wait for home page to load
#driver.save_screenshot("screenshots/03_after_login.png")

# ---------------- CLICK MENU ITEMS ---------------- #
menu_items = ["HOME", "COLLECTION", "ABOUT", "CONTACT"]

for idx, item in enumerate(menu_items, start=4):
    menu_element = wait.until(EC.presence_of_element_located((By.XPATH, f"//p[normalize-space()='{item}']")))
    driver.execute_script("arguments[0].scrollIntoView(true);", menu_element)
    time.sleep(0.5)
    driver.execute_script("arguments[0].click();", menu_element)
    print(f"Clicked menu item: {item}")
    #driver.save_screenshot(f"screenshots/0{idx}_clicked_{item}.png")
    time.sleep(1)

# ---------------- CLICK HOME AGAIN ---------------- #
home_menu = wait.until(EC.presence_of_element_located((By.XPATH, "//p[normalize-space()='HOME']")))
driver.execute_script("arguments[0].scrollIntoView(true);", home_menu)
time.sleep(0.5)
driver.execute_script("arguments[0].click();", home_menu)
print("Clicked HOME again")
#driver.save_screenshot("screenshots/08_home_again.png")
time.sleep(2)

# ---------------- CLICK PRODUCT IMAGE ---------------- #
image_element = wait.until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, "div.my-10:nth-child(2) > div:nth-child(2) > a:nth-child(1) > div:nth-child(1) > img:nth-child(1)")
    )
)
driver.execute_script("arguments[0].scrollIntoView(true);", image_element)
driver.execute_script("arguments[0].click();", image_element)
print("Clicked product image")
#driver.save_screenshot("screenshots/09_product_image.png")
time.sleep(2)

# ---------------- SELECT SIZE "M" ---------------- #
size_m_button = wait.until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[2]/div/button"))
)
driver.execute_script("arguments[0].scrollIntoView(true);", size_m_button)
driver.execute_script("arguments[0].click();", size_m_button)
print("Selected size M")
#driver.save_screenshot("screenshots/10_selected_size.png")
time.sleep(1)

# ---------------- ADD TO CART ---------------- #
add_to_cart_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'ADD TO CART')]")))
driver.execute_script("arguments[0].scrollIntoView(true);", add_to_cart_button)
driver.execute_script("arguments[0].click();", add_to_cart_button)
print("Added to cart")
#driver.save_screenshot("screenshots/11_added_to_cart.png")
time.sleep(1)

# ---------------- CLICK CART ICON ---------------- #
cart_icon = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "img[alt='Cart']")))
driver.execute_script("arguments[0].click();", cart_icon)
print("Opened cart")
#driver.save_screenshot("screenshots/12_open_cart.png")
time.sleep(1)

# ---------------- PROCEED TO CHECKOUT ---------------- #
checkout_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'PROCEED TO CHECKOUT')]")))
driver.execute_script("arguments[0].scrollIntoView(true);", checkout_button)
driver.execute_script("arguments[0].click();", checkout_button)
print("Proceeded to checkout")
#driver.save_screenshot("screenshots/13_checkout_page.png")
time.sleep(2)

# ---------------- FILL CHECKOUT FORM ---------------- #
checkout_data = {
    "firstName": "John",
    "lastName": "Doe",
    "email": "johndoe@example.com",
    "street": "123 Main Street",
    "city": "New York",
    "state": "NY",
    "zipcode": "10001",
    "country": "USA",
    "phone": "1234567890"
}

for field_name, value in checkout_data.items():
    input_element = wait.until(EC.presence_of_element_located((By.NAME, field_name)))
    driver.execute_script("arguments[0].scrollIntoView(true);", input_element)
    input_element.send_keys(value)
#driver.save_screenshot("screenshots/14_filled_checkout.png")
time.sleep(1)

# ---------------- PLACE ORDER ---------------- #
place_order_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='PLACE ORDER']")))
driver.execute_script("arguments[0].scrollIntoView(true);", place_order_button)
driver.execute_script("arguments[0].click();", place_order_button)
print("Order placed successfully!")
#driver.save_screenshot("screenshots/15_order_placed.png")
time.sleep(2)

driver.quit()
