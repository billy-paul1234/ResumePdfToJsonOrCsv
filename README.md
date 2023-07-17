# R2C & R2J
## Resume2CSV & Resume2JSON 


## ABOUT TOOL :

R2C and R2J is used to convert your resume PDF to CSV and JSON .

## AVAILABLE ON :

* Linux
* Windows
* Termux

### REQUIREMENTS :

* python3

## FEATURES :
* [+]  It will take the heading as key and the content as values for JSON.
* [+]  It will take the heading as header and the content as columns for CSV.

## INSTALLATION [Ubuntu & Termux] :
[+]--Note:- Don't delete any of the scripts

[+]--Now you need internet connection to continue further process...

* `sudo apt update -y`
* `sudo apt upgrade -y`
* `sudo apt install python3 -y`
* `sudo apt install python3-pip -y`
* `pip install "PyPDF2<3"`
* `pip install json`
* `pip install csv`
* `cd $HOME`
* `git clone https://github.com/billy-paul1234/RouterRD.git`
* `ls`
* `cd ResumeToCsvOrJson`
* `ls`
* `python R2J.py` # For pdf to json
* `python R2c.py` # For pdf to csv

[+]--Now provide your Input file (/pdf/input.pdf) and output file (/json/output.json)

[+]--Now it will generate the output file 

## SCREEN SHOTS:

Comming Soon....
![resume](https://github.com/billy-paul1234/ResumePdfToJsonOrCsv/assets/137751689/bfba578c-3b51-47ba-81f9-69d5f9383a22)

![json](https://github.com/billy-paul1234/ResumePdfToJsonOrCsv/assets/137751689/c598dd3f-b345-4aa5-a303-93fcd73ef117)
![csv](https://github.com/billy-paul1234/ResumePdfToJsonOrCsv/assets/137751689/3599bb6c-e2cb-4523-8404-22bf6e424ad1)

<!--
<br>
<p align="center">
<img width="50%" src="https://user-images.githubusercontent.com/49580304/96563949-6b90ec00-1277-11eb-9c1b-221a31d7c79d.jpg"/>
<img width="45%" src="https://user-images.githubusercontent.com/49580304/96563953-6c298280-1277-11eb-9cf2-828b351168ae.jpg"/>
<img width="50%" src="https://user-images.githubusercontent.com/49580304/96563949-6b90ec00-1277-11eb-9c1b-221a31d7c79d.jpg"/>
</p>
-->
## WATCH VIDEO:

Comming Soon....

## CONNECT ME IN:

[![Instagram](https://img.shields.io/badge/LINKEDIN-CONNECT-red?style=for-the-badge&logo=linkedin)](https://in.linkedin.com/in/billy-paul-913459270)
<!--[![Instagram](https://img.shields.io/badge/FACEBOOK-LIKE-red?style=for-the-badge&logo=facebook)]<!--(https://rebrand.ly/fsbpage)
[![Instagram](https://img.shields.io/badge/TELEGRAM-CHANNEL-red?style=for-the-badge&logo=telegram)]<!--(https://rebrand.ly/telegramchnl)
[![Instagram](https://img.shields.io/badge/WHATSAPP-JOINGROUP-red?style=for-the-badge&logo=whatsapp)]<!--(https://rebrand.ly/hckrgroups)-->


## WARNING : 
***If the heading and contents are in same line it will not take the heading as key. But in this situation it will take if the heading has colon or if the heading is in full caps.***

***EG:***

   ***Hobbies        movie, games,etc.    --> wrong format***
   
   ***Hobbies:       movies, games,etc.   --> correct format***
   
   ***HOBBIES        movies, games,etc.   --> correct format***
   
   ***This is only if the heading and content are in same line***
