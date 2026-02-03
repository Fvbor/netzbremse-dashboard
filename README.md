# netzbremse-dashboard
A small (vibe coded) dashboard for netzbremse.de

This is only a small "Dashboard" for the automatic measurements for [Netzbremse](https://netzbremse.de/).

It has only a few features and shows a few graphs, not much more.

It takes the json-results from [AKVorrat/netzbremse-measurement](https://github.com/AKVorrat/netzbremse-measurement/)

# Important:
This is a small (badly) vibe coded Dashboard.
Don´t put it into the internet without a good protection - for example a Pangolin Public Ressource with requiered Authentication for viewing this Dashboard.

# How to use:

Clone the repository and build the Container
```
cd /opt/containers
sudo git clone https://github.com/Fvbor/netzbremse-dashboard.git
cd netzbremse-dashboard
```

Change your Down-/Upstream in `app/templates/index.html` for the green area in the graphs.
It will take the Download and Upload, add/subtract 50 mbit and paint the green areas.
```
sudo nano app/templates/index.html
or vi
sudo vi app/templates/index.html
```
```
[...]
// Set here your Up- and Downstream
// For example: I have a 600/300 Down-/Upstream.
// It will show a green area on the graph around this Down-/Upstream
const download = 600
const upload = 300
const bits_to_megabits_multiplicator = 1000 * 1000
const download_upper_limit = download + 50
const download_lower_limit = download - 50 
const upload_upper_limit = upload + 50 
const upload_lower_limit = upload - 50  
[...]
```

Build the Container
```
sudo docker compose build
```

Change the path in the compose.yml to the json-results folder of your netzbremse Container.
Read Only is fine here, 

Start the Container
`sudo docker compose up -d`

Open the Dashboard in your Browser with the IP/Hostname of your Docker Server and the Port 5000
`http://netzbremse-dashboard-server:5000/`

**Again:** It is (badly) vibe coded. Don´t put it in the public internet. Only use it internal.
