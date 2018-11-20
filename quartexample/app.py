"""Example quart project.

Quart is very similar to flask but leverages async/await.
"""

from quart import Quart, websocket

app: Quart = Quart(__name__)


@app.route('/')
async def hello_world() -> str:
    """Create the home page."""
    return 'Hello world!'


@app.websocket('/ws')
async def ws():
    """Handle the WS connection."""
    while True:
        await websocket.send('hello')

if __name__ == '__main__':
    app.run('0.0.0.0', port=8000)
