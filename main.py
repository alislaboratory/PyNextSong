from NextSong import nextsong

cid = "<CID>"
secret = "<secret>"

ns = nextsong.NextSong(cid, secret)
ns.initialise()

print(ns.getRandomSong())
