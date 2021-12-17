# Web Scrapping(very very very small version)

## What is Web Scrapping ?
Have you ever wandered how many data Facebook has ? And what happens if you could access to all of it ? Well that's web scrapping, in other words is looking for apis and getting as much data as you can using scripts of course.
In Darkly, we have a small similar situation.

In `robots.txt` you will find a folder named `.hidden`. Accessing to it will give you 26 folders, each of those 26 folders has another 26 folders, and every folder in that 26 folders has another 26 folders. And for each folder in that 26 folders, there's a readme you have to read.

Meaning we have a ~= 26^3 folder which is almost 18279 readme file.

Python is a good way to solve this, check the `req.py`. After getting all the `readme` files we can use the following command to grep the flag:
```
$> grep -v -e "Demande à ton voisin du dessous" -e "Tu veux de l'aide ? Moi aussi \!" -e "Demande à ton voisin du dessus" -e "Demande à ton voisin de droite" -e "Demande à ton voisin de gauche" -e "Non ce n'est toujours pas bon ..." -e "Toujours pas tu vas craquer non ?" readme
99dde1d35d1fdd283924d84e6d9f1d820
```

## How to protect ?
You should hide your api really well. A skilled hacker can always finds them.
In our case, the `.hidden` folder shouldn't be accessible or shown in `robots.txt`.
But in general here's someways to protect against web scrapping in general:
```
Rate Limit Individual IP Addresse
Require Login For Access
Use CAPTCHA
```