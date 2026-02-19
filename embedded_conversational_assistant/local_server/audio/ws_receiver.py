import asyncio
import websockets

from local_server.nlp.summarizer import Summarizer

HOST = "0.0.0.0"
PORT = 8765

summarizer = Summarizer(
    model_name="facebook/bart-large-cnn"
)

async def handler(ws):
    print("🔗 Client connected")

    try:
        async for message in ws:
            print("📥 Received text")

            summary = summarizer.summarize(message)

            print("📤 Sending summary")
            await ws.send(summary)

    except Exception as e:
        print("❌ WS error:", e)

    finally:
        print("🔌 Client disconnected")


async def start_server():
    async with websockets.serve(handler, HOST, PORT):
        print(f"🚀 WS server running at ws://{HOST}:{PORT}")
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(start_server())
