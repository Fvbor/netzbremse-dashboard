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
sudo docker compose build
```

Change the path in the compose.yml to the json-results folder of your netzbremse Container.
Read Only is fine here, 

Start the Container
`sudo docker compose up -d`

Open the Dashboard in your Browser with the IP/Hostname of your Docker Server and the Port 5000
`http://netzbremse-dashboard-server:5000/`

**Again:** It is (badly) vibe coded. Don´t put it in the public internet. Only use it internal.
