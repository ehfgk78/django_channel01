from channels.routing import route

from example.consumer import ws_connect, ws_disconnect

channel_routing = [
    route('websocket.connect', ws_connect),
    route('websocket.disconnect', ws_disconnect),
]

# 에러 1::  An outdated asgi_redis package was the issue.
# Error trying to receive messages: name 'txredisapi' is not defined
#   An outdated asgi_redis package was the issue.
#   I was just checking the package listing in PyCharm,
#   which didn't show me the newer version, ' \
#   'so I thought I was on the latest version without checking the CheeseShop

# 에러 2::  Redis Server Problems...Unable to Connect localhost:6379 - Build ...
# sudo apt-get install redis-server
# sudo service redis-server start|stop|restart|force-reload|status