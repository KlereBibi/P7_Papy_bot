from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Créer une session Firefox
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()

# Appeler l’application web
driver.get("http://127.0.0.1:5000/")

# Localiser la zone de texte
search_field = driver.find_element(By.ID, "userText")
search_field.clear()

# Saisir et confirmer le mot-clé
search_field.send_keys("Claire")
search_field.submit()


response = driver.find_element(By.ID, "answer")

print(response)

# Fermer la fenêtre du navigateur
driver.quit()