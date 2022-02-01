
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_fonctionnal_application():
    # Créer une session Firefox
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    driver.implicitly_wait(30)

    # Appeler l’application web
    driver.get("http://127.0.0.1:5000/")

    # Localiser la zone de texte
    search_field = driver.find_element(By.ID, "userText")
    search_field.clear()

    # Saisir et confirmer le mot-clé
    search_field.send_keys("Claire")
    search_field.submit()

    response = driver.find_element(By.CLASS_NAME, "papy").text

    expected_value = "Mes petites cellules grises se souviennent que: Le Claire est une ville située dans le comté de Scott, dans l’État de l’Iowa, aux États-Unis. Lors du recensement de 2010, sa population s’élevait à 3 765 habitants."

    assert response == expected_value

    # Fermer la fenêtre du navigateur
    