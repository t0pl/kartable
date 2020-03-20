# Kartable
Generate a free kartable.fr account the easy way.
I'm trying to create a sort of non-official API for [kartable.fr](https://www.kartable.fr)

### Prerequisites
I've only tested on Windows with chrome installed, but you can definitely use firefox
I guess you need a OS that has a graphical interface (not sure) and maybe only Python 3 (or later) works.
The [helium](https://github.com/mherrmann/helium) module is needed as well, it's a useful wrapper for the [selenium](https://pypi.org/project/selenium/) module
```
pip install helium
```
### Usage
```
python -i kartable.py
instance = main("6e","philotea","ons","manlymprinc1241478451ent@gmail.com","xfcgvhibu1457hoomskpjoihugyf")
instance.register()
instance.log_out()
instance.join_school()
...
```
Or
```
import kartable
...
```
### What you have to know about kartable.fr
It's a French learning platform, with so many lessons, exercices, videos and stuff.
It offers the opportunity to get 10 resources for free and it has a gamified system based on "rubies": if you click on a resource, you'll have one less ruby but you can get some if you complete some missions called "Mini-quêtes", and there's obviously a way to complete them automatically.

## Improvements
I know there are three account's types available ("élève", "parent", "professeur"), but I have only implemented the first one.
### TODO
* get a file or sth with all the lessons, levels, subjects available or not, like the tree command on linux/windows
* confirm email address properly via a temporary mail provider
* create several accounts quickly to get more rubies ([sponsorship](https://www.kartable.fr/compte/parrainage?questIdentifier=sponsorship_fifth))
* change [personal info](https://www.kartable.fr/compte/informations-personnelles) (email, password, name,...)
* save a lesson properly (with links and stuff available)
* connect with facebook
* handle "forgot your password?"
* export cookies or credentials easily
* easily choose chrome or firefox, or maybe detect
* make it open the webbrowser headlessly first to get everything, and open again
* prevent the use of empty strings in main class
* figure out how the [activation](https://www.kartable.fr/compte/activer-un-code-abonnement) process to connect as a premium member works 


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
