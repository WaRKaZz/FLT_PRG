import asyncio

import edge_tts

VOICE = "kk-KZ-AigulNeural"
OUTPUT_FOLDER = "C:\\Intel\\PRJ\\FLT_PRG\\resources\\voice_aigul"


async def main(text) -> None:
    """Main function"""
    communicator = edge_tts.Communicate(text, VOICE)
    await communicator.save(OUTPUT_FOLDER + f"\\{text}.mp3")


if __name__ == "__main__":
    for i in range(1001):
        asyncio.run(main(str(i)))
    for i in range(10):
        asyncio.run(main(f"00{i}"))
    for i in range(10, 100):
        asyncio.run(main(f"0 {i}"))
    asyncio.run(main("плюс 7"))
        