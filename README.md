# Simple chat app with Python socket

### Server

```
Home> python .\server.py

[SERVER] Server is starting...
[SERVER] Server is listening on :5656
-----------------------------------------

[NEW CONNECTION] ('192.168.1.24', 63893) CONNECTED!
[ACTIVE CONNECTIONS] 1

[ Doraemon ] Hello! I am Doraemon.

[NEW CONNECTION] ('192.168.1.24', 63894) CONNECTED!
[ACTIVE CONNECTIONS] 2

[ Nobita ] What the hell r you doing here?
[ Nobita ] Get out of this chat now!
[ Nobita ] We got work to do!
-- Nobita -- has exited!
[ Doraemon ] OK ok!
-- Doraemon -- has exited!
Home>
```

### Client 1

```
Home> python .\client.py

Your username > Doraemon
[SERVER] Server is listening to you...
Your msg > Hello! I am Doraemon.
Your msg > OK ok!
Your msg > !D
------------------ End session! ------------------
Home>
```

### Client 2

```
Home> python .\client.py

Your username > Nobita
[SERVER] Server is listening to you...
Your msg > What the hell r you doing here?
Your msg > Get out of this chat now!
Your msg > We got work to do!
Your msg > !D
------------------ End session! ------------------
Home>
```

```
    Nguyen Thanh Hung
```
