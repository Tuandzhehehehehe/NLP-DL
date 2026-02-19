import asyncio
import websockets

from nlp.summarizer import Summarizer

# =====================
# CONFIG
# =====================
HOST = "0.0.0.0"
PORT = 8765
SUMMARY_MODEL = "facebook/bart-large-cnn"

# =====================
# LOAD MODEL
# =====================
print("🔄 Loading summarization model...")
summarizer = Summarizer(SUMMARY_MODEL)
print("✅ Summarization model loaded")


# =====================
# WS HANDLER
# =====================
async def handler(ws):
    print("🟢 Client connected")

    async for message in ws:
        try:
            print("📩 Received:", type(message))

            # -------- TEXT --------
            if isinstance(message, str):
                print("📝 Text input received")
                summary = summarizer.summarize(message)

                await ws.send(summary)
                print("📤 Summary sent")

            # -------- AUDIO (future) --------
            elif isinstance(message, bytes):
                await ws.send("Audio received (not processed yet)")

            else:
                await ws.send("Unsupported data type")

        except Exception as e:
            print("❌ SERVER ERROR:", e)
            await ws.send(f"ERROR: {e}")


# =====================
# MAIN LOOP
# =====================
async def main():
    print(f"🌐 WebSocket listening on ws://{HOST}:{PORT}")
    async with websockets.serve(handler, HOST, PORT):
        print("🚀 Local server running")
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
