import socket
import logging
import urllib.parse


config = {
    "archive": {
        "url_download": "https://archive.org/download/",
        "url_servicesimg": "https://archive.org/services/img/",
        "url_metadata": "https://archive.org/metadata/",
        "url_btihsearch": 'https://archive.org/advancedsearch.php?fl=identifier,btih&output=json&rows=1&q=btih:',
    },
    "ipfs": {
        "url_add_data": "http://localhost:5001/api/v0/add", # FOr use on gateway or if run "ipfs daemon" on test machine
        # "url_add_data": "https://ipfs.dweb.me/api/v0/add",  # note Kyle was using localhost:5001/api/v0/add which wont resolve externally.
        # "url_add_url": "http://localhost:5001/api/v0/add",  #TODO-IPFS move uses of url_add_data to urladd when its working
        #"url_urlstore": "http://localhost:5001/api/v0/urlstore/add",    # FOr use on gateway or if run "ipfs daemon" on test machine
        "url_dht_provide": "http://localhost:5001/api/v0/dht/provide",
    },
    "gateway": {
        "url_download": "https://dweb.me/arc/archive.org/download/",
        "url_servicesimg": "https://dweb.me/arc/archive.org/thumbnail/",
        "url_torrent": "https://dweb.me/arc/archive.org/torrent/",
    },
    "domains": {
        # This is also name of directory in /usr/local/dweb-gateway/.cache/table, if change this then can safely rename that directory to new name to retain metadata saved
        "metadataverifykey": 'NACL VERIFY:h9MB6YOnYEgby-ZRkFKzY3rPDGzzGZ8piGNwi9ltBf0=',
        "metadatapassphrase": "Replace this with something secret/arc/archive.org/metadata",                       # TODO - change for something secret!
        "directory": '/usr/local/dweb-gateway/.cache/table/',                             # Used by maintenance note overridden below for mitraglass (mitra's laptop)
    },
    "directories": {
        "bootloader": "/usr/local/dweb-transport/examples/bootloader.html",               # Location of bootloader file, note overridden below for mitraglass (mitra's laptop)
    },
    "logging": {
        "level": logging.DEBUG
    },  # By default Not to file - overridden below for dev machine
    "ignoreurls": [ # Ignore these, they are hacks or similar
        urllib.parse.unquote("%E2%80%9D"),
        "robots.txt",   #Not a hack, but we dont have one TODO
    ]

}

if socket.gethostname() in ["wwwb-dev0.fnf.archive.org"]:
    config["ipfs"]["url_urlstore"] = "http://localhost:5001/api/v0/urlstore/add" # Only runs in beta on archive.org research machine
    config["logging"] = { "filename": 'dweb-gateway.log', "level": logging.DEBUG }  #Not to file
elif socket.gethostname().startswith('mitraglass'):
    # TODO make sure to remove url_urlstore defnt !
    config["ipfs"]["url_urlstore"] = "http://localhost:5001/api/v0/urlstore/add" # Only runs in beta on archive.org research machine
    config["directories"]["bootloader"] = "/Users/mitra/git/dweb-archive/bootloader.html"
    config["domains"]["directory"] = "/Users/mitra/git/dweb-gateway/.cache/table/"
else:
    print("Needs configuring for {}".format(socket.gethostname()))

