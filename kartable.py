import helium
import hashlib

driver = helium.start_chrome("https://temp-mail.org/en/",headless=True)
helium.wait_until(lambda: "@" in helium.TextField(
    "Your Temporary email address").value)
email = helium.TextField("Your Temporary email address").value
password = hashlib.sha1(email.encode()).hexdigest()
print(email,password)
helium.kill_browser()
driver = helium.start_chrome("https://www.kartable.fr/inscription")
helium.click("élève")
helium.click("1ère")
helium.click("s'inscrire avec un e-mail")
helium.write("Cld",into="prénom")
helium.write("Lokidod",into="nom")
helium.write(email,into="adresse e-mail")
helium.write(password,into="mot de passe")
helium.click("terminer")
helium.wait_until(helium.Text("plus tard").exists)
helium.click("plus tard")
#helium.kill_browser()