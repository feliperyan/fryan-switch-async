import asyncio
from quart import Quart, request

app = Quart(__name__)

@app.route('/', methods=['GET'])
async def sleep():
    await asyncio.sleep(4)
    print("received request")
    return 'Slept for 400ms'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
