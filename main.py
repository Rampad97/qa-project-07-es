import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    taxi_button = (By.XPATH, data.taxi)
    comfort_button = (By.XPATH, data.comfort)
    phone_button = (By.CLASS_NAME, 'np-button')
    phone_field = (By.ID, 'phone')
    next_button = (By.XPATH, data.next)
    phone_code = (By.ID, 'code')
    confirm_button = (By.XPATH, data.confirm_code)
    payment_button = (By.CSS_SELECTOR, '.pp-button.filled')
    add_card_button = (By.CSS_SELECTOR, '.pp-row.disabled')
    number_card_field = (By.ID, 'number')
    code_card_field = (By.XPATH, data.payment_code)
    link_button = (By.XPATH, data.link_card)
    close_window_button = (By.XPATH, data.close_payment)
    comment_field = (By.ID, 'comment')
    slide_button = (By.CLASS_NAME, 'slider.round')
    ice_cream = (By.XPATH, data.counter_plus)
    order_taxi_button = (By.CSS_SELECTOR, '.smart-button')
    modal_element = (By.CSS_SELECTOR, '.order-header-content')

    def __init__(self, driver):
        self.driver = driver

    #Ingresar dirección "From" (Desde)
    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    #Ingresar dirección "To" (Hasta)
    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    #Click en el botón para pedir el taxi
    def click_taxi_button(self):
        self.driver.find_element(*self.taxi_button).click()

    #Click para seleccionar el tipo de transporte "Comfort"
    def click_comfort_button(self):
        self.driver.find_element(*self.comfort_button).click()

   #Campo "Agregar número de teléfono"
    def set_phone_number(self, phone):
        self.driver.find_element(*self.phone_button).click()    #Click en el campo "agregar número"
        self.driver.find_element(*self.phone_field).send_keys(phone)    #Escribir el número de teléfono
        self.driver.find_element(*self.next_button).click()                    #Click en el botón siguiente

    #Introducir código SMS
    def set_confirmation_code(self):
        self.driver.find_element(*self.phone_code).send_keys(retrieve_phone_code(self.driver))  #Agregar código
        self.driver.find_element(*self.confirm_button).click()             #Confirmar código

    #Campo agregar "Forma de pago"
    def set_payment_method(self, card, code_card):
        self.driver.find_element(*self.payment_button).click()      #Click para abrir la ventana "Forma de pago"
        self.driver.find_element(*self.add_card_button).click()     #Click en el botón para agregar una tarjeta
        self.driver.find_element(*self.number_card_field).send_keys(card)       #Agregar número tarjeta
        self.driver.find_element(*self.code_card_field).send_keys(code_card)     #Agregar código
        self.driver.find_element(*self.code_card_field).send_keys(Keys.TAB)     #Confirmar código
        self.driver.find_element(*self.link_button).click()                     #Click en el botón enlace
        self.driver.find_element(*self.close_window_button).click()             #Cerrar ventana

    #Agregar comentario
    def set_comment(self, message):
        self.driver.find_element(*self.comment_field).send_keys(message)            #Click en el campo de comentarios
        return self.driver.find_element(*self.comment_field).get_property('value')

    #Pedir una manta y pañuelos
    def get_manta_panuelos(self):
        self.driver.find_element(*self.slide_button).click()

    #Pedir 2 helados
    def get_ice_2_cream(self):
        self.driver.find_element(*self.ice_cream).click()
        self.driver.find_element(*self.ice_cream).click()

    #Click en el botón para ordenar el taxi
    def click_order_taxi_button(self):
        self.driver.find_element(*self.order_taxi_button).click()

    #Esperar a que aparezca la información del conductor en el modal
    def wait_for_load_information(self):
        WebDriverWait(self.driver, 35).until(EC.presence_of_element_located(self.modal_element))

class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

        routes_page.click_taxi_button()
        routes_page.click_comfort_button()

        phone = data.phone_number
        routes_page.set_phone_number(phone)

        routes_page.set_confirmation_code()

        card = data.card_number
        code_card = data.card_code
        routes_page.set_payment_method(card, code_card)

        message = data.message_for_driver
        routes_page.set_comment(message)

        routes_page.get_manta_panuelos()
        routes_page.get_ice_2_cream()
        routes_page.click_order_taxi_button()
        routes_page.wait_for_load_information()


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

if __name__ == '__main__':
    test_valid = TestUrbanRoutes()
    test_valid.setup_class()
    test_valid.teardown_class()