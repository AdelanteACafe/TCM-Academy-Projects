#!/bin/bash


#This is from the scripting section of the Practical Ethical Hacking course (PEH)
#This script has been tested and works perfectly
#In the future I will find and test more python based scripts (and less Go) so as to have a script that will function without having to install Go and other languages onto a fresh Kali/Parrot install.
url=$1
#$1 refers to the 1st argument

#if the directory doesnt exist, go ahead and make it
if [ ! -d "$url" ];then
	mkdir $url
fi
#if the directory/folder doesnt exist, go ahead and make it
if [ ! -d "$url/recon" ];then
	mkdir $url/recon
fi

echo "[+] Harvesting subdomains with Assetfinder..."
assetfinder $url >> $url/recon/assets.txt

#The following will filter out only subdomains in scope
#remember "$1" is the 1st argument, that is, the target website
cat $url/recon/assets.txt | grep $1 >> $url/recon/final.txt


#Confirmed. This works perfectly

#Syntax is:
#./run.sh target sitio

#Runs Assetfinder (must be installed) makes directories and folders, limits results to target site
#This is beautiful

#---------------------syntax below adds Amass functionality to the script--------------------------------

#echo "[+] Harvesting subdomains with Amass..."
#amass enum -d $url >> $url/recon/f.txt
#above is simply the syntax to run amass, and results are sent to recon folder and saved in a file

#sort -u $url/recon/f.txt >> $url/recon/final.txt
#this sorts the data as done with Assetfinder
#rm $url/recon/f.txt
#honestly, not sure what rm command is for yet

#at end of Amass vid teacher comments Amass section out, says we no use this rest of course, no se
#but ive confirmed my code is accurate


#-----------------------------------------below is next tool, Httprobe---------------------------------


echo "[+] Probing for alive domains with Httprobe..."

cat $url/recon/final.txt | sort -u | httprobe -s -p https:443 | sed 's/https\?:\/\///' | tr -d ':443' >> $url/recon/alive.txt
#sort -u is for unique, this will filter out duplicates
#syntax with httprobe deals with conflicts related to automated dns, issue teacher knew he'd have
#dont think i will but included for completeness, can coment out if needed, veamos

#works beautifully :)



#-----------------------------------Final Tool Go Witness----------------------------------------------
#this one is tad different, it not a probe, this automatically takes screenshots of the targets

gowitness single https://tesla.com

#everything worked like teacher said but pic always came in blank (even he had to repeat process twice)
#no se











